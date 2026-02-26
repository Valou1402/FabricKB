# FabricKB 🧠

**Personal Microsoft Fabric knowledge base — auto-generated from Readwise.**

Every article saved to Readwise is automatically fetched, summarized by Claude AI, and compiled into a single structured markdown file that can be fed as context to Claude at the start of any working session.

## How it works

```
Readwise Reader (browser extension)
        ↓  save article
GitHub Actions (every 6 hours)
        ↓  fetch via Readwise API
        ↓  summarize via Claude API (summary + key concepts + code flag)
        ↓  write FABRIC_KNOWLEDGE.md
        ↓  commit & push
FABRIC_KNOWLEDGE.md (public raw URL)
        ↓  "Fetch my Fabric knowledge base"
Claude session — full knowledge context loaded
```

## Setup (one-time)

### 1. Add GitHub Secrets

Go to **Settings → Secrets and variables → Actions → New repository secret** and add:

| Secret name | Where to get it |
|---|---|
| `READWISE_TOKEN` | https://readwise.io/access-token |
| `ANTHROPIC_API_KEY` | https://console.anthropic.com/settings/keys |

### 2. Enable GitHub Actions

Go to **Actions** tab and enable workflows if prompted.

### 3. Trigger first run

Go to **Actions → Update FabricKB Knowledge Base → Run workflow** to trigger immediately rather than waiting for the schedule.

## Your knowledge base URL

Once the repo is public, your raw knowledge file URL will be:

```
https://raw.githubusercontent.com/YOUR_USERNAME/FabricKB/main/FABRIC_KNOWLEDGE.md
```

Replace `YOUR_USERNAME` with your GitHub username.

## Using with Claude

At the start of any Microsoft Fabric working session, tell Claude:

> "Please fetch my Fabric knowledge base from: https://raw.githubusercontent.com/YOUR_USERNAME/FabricKB/main/FABRIC_KNOWLEDGE.md"

Claude will ingest all your curated articles and use them as live context for the session.

## Files

| File | Purpose |
|---|---|
| `update_knowledge.py` | Main pipeline script |
| `FABRIC_KNOWLEDGE.md` | The generated knowledge base (auto-updated) |
| `.processed_ids.json` | Cache of processed article IDs (avoids re-calling Claude API) |
| `requirements.txt` | Python dependencies |
| `.github/workflows/update_knowledge.yml` | GitHub Actions schedule |

## Cost estimate

With 5–15 new articles/week and Claude Sonnet:
- ~$0.01–0.05 per article summary
- **~$0.05–0.75/week** in API costs
- Already-processed articles are cached and never re-billed
