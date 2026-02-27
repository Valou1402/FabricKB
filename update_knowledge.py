#!/usr/bin/env python3
"""
FabricKB - Readwise → Claude → GitHub Knowledge Pipeline
Fetches all articles from Readwise, generates AI summaries via Claude API,
and writes a structured FABRIC_KNOWLEDGE.md file.
"""

import os
import json
import re
import requests
from datetime import datetime, timezone
from anthropic import Anthropic

# ── Config ──────────────────────────────────────────────────────────────────
READWISE_TOKEN = os.environ["READWISE_TOKEN"]
ANTHROPIC_API_KEY = os.environ["ANTHROPIC_API_KEY"]
OUTPUT_FILE = "FABRIC_KNOWLEDGE.md"
STATE_FILE = ".processed_ids.json"  # tracks already-processed article IDs

client = Anthropic(api_key=ANTHROPIC_API_KEY)


# ── Readwise helpers ─────────────────────────────────────────────────────────
def fetch_all_readwise_documents():
    """Fetch all documents from Readwise Reader (paginated)."""
    docs = []
    url = "https://readwise.io/api/v3/list/"
    headers = {"Authorization": f"Token {READWISE_TOKEN}"}
    params = {"category": "article", "page_size": 100}

    while url:
        resp = requests.get(url, headers=headers, params=params, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        docs.extend(data.get("results", []))
        url = data.get("next")
        params = {}  # next URL already contains params

    return docs


def is_reader_doc_id(doc_id):
    """Reader documents use alphanumeric IDs (e.g. 01kjf01q4r51p60rszajkc1p4k).
    Classic Readwise books use numeric integer IDs. Only numeric IDs work with v2 API."""
    return not str(doc_id).isdigit()


def fetch_readwise_highlights(doc_id):
    """Fetch highlights for a classic Readwise document (numeric ID only).
    Reader documents (alphanumeric IDs) don't support the v2 highlights endpoint."""
    if is_reader_doc_id(doc_id):
        return []  # Reader docs — highlights not available via v2 API

    url = "https://readwise.io/api/v2/highlights/"
    headers = {"Authorization": f"Token {READWISE_TOKEN}"}
    params = {"book_id": doc_id, "page_size": 100}
    highlights = []

    while url:
        resp = requests.get(url, headers=headers, params=params, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        highlights.extend(data.get("results", []))
        url = data.get("next")
        params = {}

    return [h["text"] for h in highlights if h.get("text")]


# ── Claude helpers ───────────────────────────────────────────────────────────
def extract_code_snippets(text):
    """Pull out fenced code blocks from raw content."""
    if not text:
        return []
    pattern = r"```[\w]*\n(.*?)```"
    return re.findall(pattern, text, re.DOTALL)


def generate_entry(doc):
    """Call Claude to produce summary, key concepts, and flag code snippets."""
    title = doc.get("title") or "Untitled"
    url = doc.get("source_url") or doc.get("url") or ""
    summary_text = doc.get("summary") or ""
    content = doc.get("content") or ""
    highlights = doc.get("_highlights", [])

    # Build input for Claude — prefer content, fall back to summary + highlights
    source_material = ""
    if content:
        source_material = content[:6000]  # stay within token budget
    elif summary_text:
        source_material = summary_text
    if highlights:
        source_material += "\n\nHighlights:\n" + "\n".join(f"- {h}" for h in highlights[:15])

    if not source_material.strip():
        source_material = f"Title: {title}\nURL: {url}"

    prompt = f"""You are a Microsoft Fabric technical knowledge assistant.

Analyse the following article and return a JSON object with exactly these keys:
- "summary": 2-3 sentence technical summary focused on what is useful for a Fabric practitioner
- "key_concepts": list of 3-8 short concept strings (e.g. "Lakehouse", "Delta tables", "Workspace governance")
- "has_code": boolean, true if the article contains code examples or KQL/SQL/Python/PySpark/DAX snippets
- "code_language": string, primary language if has_code is true, else null

Return ONLY valid JSON, no markdown fences, no explanation.

Article title: {title}
Article URL: {url}

Content:
{source_material}
"""

    try:
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=512,
            messages=[{"role": "user", "content": prompt}],
        )
        raw = message.content[0].text.strip()
        # Strip markdown fences if model adds them anyway
        raw = re.sub(r"^```json\s*", "", raw)
        raw = re.sub(r"```$", "", raw).strip()
        return json.loads(raw)
    except Exception as e:
        print(f"  ⚠️  Claude API error for '{title}': {e}")
        return {
            "summary": summary_text or "Summary not available.",
            "key_concepts": [],
            "has_code": False,
            "code_language": None,
        }


# ── Markdown rendering ───────────────────────────────────────────────────────
def format_entry(doc, ai):
    """Render a single article as a markdown section."""
    title = doc.get("title") or "Untitled"
    url = doc.get("source_url") or doc.get("url") or ""
    saved_at = doc.get("created_at") or doc.get("saved_at") or ""
    if saved_at:
        try:
            saved_at = datetime.fromisoformat(saved_at.replace("Z", "+00:00")).strftime("%Y-%m-%d")
        except Exception:
            pass

    source = doc.get("domain") or doc.get("source") or ""

    lines = [f"## [{title}]({url})"]
    meta_parts = []
    if saved_at:
        meta_parts.append(f"📅 {saved_at}")
    if source:
        meta_parts.append(f"🌐 {source}")
    if meta_parts:
        lines.append(" · ".join(meta_parts))
    lines.append("")

    summary = ai.get("summary", "")
    if summary:
        lines.append(f"**Summary:** {summary}")
        lines.append("")

    concepts = ai.get("key_concepts", [])
    if concepts:
        lines.append(f"**Key Concepts:** {', '.join(concepts)}")
        lines.append("")

    if ai.get("has_code"):
        lang = ai.get("code_language") or "code"
        lines.append(f"**Contains Code:** ✅ ({lang})")
        lines.append("")

    highlights = doc.get("_highlights", [])
    if highlights:
        lines.append("**Highlights:**")
        for h in highlights[:5]:
            lines.append(f"> {h}")
        lines.append("")

    lines.append("---")
    return "\n".join(lines)


# ── State management (avoid re-processing) ───────────────────────────────────
def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f:
            return json.load(f)
    return {}


def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


# ── Main ─────────────────────────────────────────────────────────────────────
def main():
    print("🔍 Fetching documents from Readwise...")
    docs = fetch_all_readwise_documents()
    print(f"   Found {len(docs)} documents total.")

    state = load_state()
    new_count = 0

    # Sort newest first by created_at
    docs.sort(key=lambda d: d.get("created_at") or "", reverse=True)

    enriched = []
    for doc in docs:
        doc_id = str(doc.get("id"))
        title = doc.get("title") or "Untitled"

        if doc_id in state:
            # Already processed — reuse cached AI output
            doc["_highlights"] = state[doc_id].get("highlights", [])
            doc["_ai"] = state[doc_id]["ai"]
            enriched.append(doc)
            continue

        print(f"  ✨ Processing new: {title[:60]}")
        highlights = fetch_readwise_highlights(doc_id)
        doc["_highlights"] = highlights
        ai = generate_entry(doc)
        doc["_ai"] = ai

        state[doc_id] = {
            "title": title,
            "ai": ai,
            "highlights": highlights,
            "processed_at": datetime.now(timezone.utc).isoformat(),
        }
        enriched.append(doc)
        new_count += 1

    save_state(state)
    print(f"   {new_count} new articles processed, {len(enriched) - new_count} loaded from cache.")

    # ── Build markdown file ──────────────────────────────────────────────────
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    header = f"""# 🧠 FabricKB — Microsoft Fabric Knowledge Base

> Auto-generated from Valentin's Readwise library · Last updated: {now}
> {len(enriched)} articles · Newest first
>
> **How to use:** Share the raw URL of this file with Claude at the start of any Fabric session.

---

"""

    entries = [format_entry(doc, doc["_ai"]) for doc in enriched]
    content = header + "\n\n".join(entries) + "\n"

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ {OUTPUT_FILE} written — {len(enriched)} articles.")


if __name__ == "__main__":
    main()
