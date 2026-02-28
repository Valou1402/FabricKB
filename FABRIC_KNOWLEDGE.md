# 🧠 FabricKB — Microsoft Fabric Knowledge Base

> Auto-generated from Valentin's Readwise library · Last updated: 2026-02-28 06:42 UTC
> 79 articles · Newest first
>
> **How to use:** Share the raw URL of this file with Claude at the start of any Fabric session.

---

## [Eureka - making %pip install work in child notebooks](https://www.reddit.com/r/MicrosoftFabric/comments/1jl4wzt/eureka_making_pip_install_work_in_child_notebooks/?share_id=WNvYST8vbv48eTl1vMVtd&utm_content=2&utm_medium=ios_app&utm_name=iossmf&utm_source=share&utm_term=22)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** A workaround enables dynamic Python package installation in child notebooks by using get_ipython().run_line_magic() instead of %pip install. This solution helps developers avoid long environment startup times during development and testing phases.

**Key Concepts:** Child notebooks, Dynamic package installation, notebookutils.notebook.run, Development workflows, Environment management

**Contains Code:** ✅ (Python)

---

## [Open Mirroring - Anyone using in production?](https://www.reddit.com/r/MicrosoftFabric/comments/1oplua7/open_mirroring_anyone_using_in_production/?share_id=g__KLR7paL1NuOc_0LUof&utm_content=2&utm_medium=ios_app&utm_name=iossmf&utm_source=share&utm_term=22)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** Open Mirroring in Microsoft Fabric shows promise as a game-changing feature but faces production challenges including silent replication failures and performance issues. Some teams are successfully using it in production with workarounds like append-only ingestion and careful log monitoring.

**Key Concepts:** Open Mirroring, Replication monitoring, Append-only ingestion, Production deployment, Performance optimization

---

## [Claude + Power BI Integration MASSIVE Breakthrough via MCP (Nov 2025 Update)](https://www.reddit.com/r/PowerBI/comments/1pcitfq/claude_power_bi_integration_massive_breakthrough/?share_id=gdaFYGiz5EjiOmSVw_s2n&utm_content=2&utm_medium=ios_app&utm_name=iossmf&utm_source=share&utm_term=22)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** The November 2025 Power BI update introduces direct Claude AI integration through MCP for automated DAX creation, metadata improvement, and data dictionary generation. This integration enables AI-powered automation for Power BI models but requires careful verification to ensure accuracy.

**Key Concepts:** Claude AI integration, DAX automation, Metadata management, Data dictionaries, AI-powered modeling, MCP protocol

---

## [Polars sink_delta to onelake is a Big Deal](https://www.reddit.com/r/MicrosoftFabric/comments/1q9wuoi/polars_sink_delta_to_onelake_is_a_big_deal/?share_id=JlsiL7Ys-4VQHJJFicBBA&utm_content=2&utm_medium=ios_app&utm_name=iossmf&utm_source=share&utm_term=22)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** Polars introduced a sink_delta feature that enables streaming data to OneLake in small batches, allowing efficient processing of large CSV files with limited memory resources. This capability provides performance advantages over other engines like DuckDB for small data scenarios in Fabric environments.

**Key Concepts:** Polars, OneLake, Delta streaming, Memory optimization, CSV processing, Data ingestion

---

## [How to add unit tests for notebooks](https://www.reddit.com/r/MicrosoftFabric/comments/1qft2yq/how_to_add_unit_tests_for_notebooks/?share_id=yhq0D8TIa54a9YDUKDX-M&utm_content=2&utm_medium=ios_app&utm_name=iossmf&utm_source=share&utm_term=22)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** Unit testing Fabric notebooks is challenging due to their interactive nature and global dependencies. The recommended approach is to extract business logic into separate testable modules (wheels) while keeping notebooks as simple execution entry points.

**Key Concepts:** Notebooks, Unit testing, Python modules, Wheels, Business logic separation, Code maintainability

---

## [Surge protection gets smarter: introducing workspace-level controls (Preview)](https://www.reddit.com/r/MicrosoftFabric/comments/1qnncmc/surge_protection_gets_smarter_introducing/?share_id=bspBsVNYnzI3u1oxymtUs&utm_content=2&utm_medium=ios_app&utm_name=iossmf&utm_source=share&utm_term=22)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** Microsoft Fabric has introduced workspace-level surge protection controls that limit capacity consumption per workspace over 24-hour periods. This feature helps prevent background operations from causing throttling issues, though it may not address short-term interactive usage spikes.

**Key Concepts:** Workspace governance, Surge protection, Capacity management, Throttling prevention, Background operations

---

## [Transitioning to the New Power BI Enhanced Report Format (PBIR) - What You Need to Know](https://www.reddit.com/r/MicrosoftFabric/comments/1qxh7iq/transitioning_to_the_new_power_bi_enhanced_report/?share_id=hYhPenmDHgf8nUMwjdqwX&utm_content=2&utm_medium=ios_app&utm_name=iossmf&utm_source=share&utm_term=22)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** Microsoft is transitioning to PBIR as the default format for Power BI reports to improve source control integration and reduce merge conflicts. The format enhances automation capabilities and makes reports more readable for version control, though conversion is difficult to reverse and currently in preview status.

**Key Concepts:** PBIR format, Power BI reports, Source control integration, Merge conflict reduction, Report automation, Version control

---

## [Open Mirroring Full Drop](https://www.reddit.com/r/MicrosoftFabric/comments/1qzufgs/open_mirroring_full_drop/?share_id=nuvscPeLbCNjedCuVmt0E&utm_content=2&utm_medium=ios_app&utm_name=iossmf&utm_source=share&utm_term=22)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** Open Mirroring tables can be fully reset by deleting the entire LandingZone folder, which will drop the mirrored table after a brief delay. The system operates asynchronously, so there's a normal wait time before the table is recreated from the source.

**Key Concepts:** Open Mirroring, LandingZone folder, Table reset, Asynchronous sync, Mirror tables

---

## [Sean Kallenberg’s Post](https://www.linkedin.com/posts/sean-kallenberg-25323214b_onelake-fabric-recipessamplecodepurepythondeltatableloadpy-activity-7433104995539030016-9rz3?utm_source=share&utm_medium=member_desktop&rcm=ACoAAA4TApsBpcD7dMto9tdEqMhSTfRhiYAy83E)
📅 2026-02-27 · 🌐 Reader add from import URL

**Summary:** Teams often overspend on Microsoft Fabric due to incorrect initial capacity unit (CU) sizing. Cost optimization requires careful CU monitoring, proper pause timing, appropriate compute type selection, and a start-small-then-scale approach.

**Key Concepts:** Capacity units, Cost optimization, Compute sizing, Capacity monitoring, Fabric pricing

---

## [How Janus Henderson built a hybrid Snowflake-Databricks architecture](https://www.linkedin.com/feed/update/urn:li:activity:7374108757531947008?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7374108757531947008%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** Analysts and business users rely on Snowflake for fast, governed insights.

Data engineers and scientists work in Databricks to build transformations, streaming pipelines, and ML models.

This division of personas is why many enterprises run both platforms together.

Each environment plays to its strengths — but the challenge is creating a unified architecture where workloads, governance, and costs remain in balance.

Architectural patterns, such as Medallion Architecture, help bridge the gap by aligning raw, curated, and business-ready layers across Snowflake and Databricks into a consistent lifecycle.

In practice, this means:

- Raw (Bronze): Data is ingested into Databricks, where engineers and scientists handle transformations and model training.

- Curated (Silver): Cleaned and standardized data flows through pipelines, creating a consistent layer that bridges Databricks and Snowflake.

- Business-Ready (Gold): Governed datasets are published in Snowflake for analysts and business users to query with confidence

Join us today at 1 PM ET to learn how our client Janus Henderson Investors brought this architecture to life — combining both platforms into a scalable, governed, and cost-efficient hybrid environment.

Register here: https://lnkd.in/gvYCUY44

You’ll hear from Wayne Eckerson, Michael Spiessbach, and Mark Goodwin. 

#UnifiedArchitecture

---

## [Kurt Buhler’s Post](https://www.linkedin.com/feed/update/urn:li:activity:7383401120087576576?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7383401120087576576%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** Choosing a storage mode for your Power BI model is very important, but can be confusing. This article gives you an overview, some key considerations, and a few tips: https://lnkd.in/e6jayjd2


The quick reference image here is high-level. Check the article for details, references, and other resources.

#MicrosoftFabric #PowerBI #StorageMode #Godot | 11 comments on LinkedIn

---

## [Marc Lelijveld’s Post](https://www.linkedin.com/feed/update/urn:li:activity:7383857817704734720?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7383857817704734720%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** 🚀 𝗔𝘂𝘁𝗼𝗺𝗮𝘁𝗶𝗻𝗴 𝗣𝗼𝘄𝗲𝗿 𝗕𝗜 𝗦𝗲𝗺𝗮𝗻𝘁𝗶𝗰 𝗠𝗼𝗱𝗲𝗹 𝗦𝗲𝗰𝘂𝗿𝗶𝘁𝘆 𝘄𝗶𝘁𝗵 𝗙𝗮𝗯𝗿𝗶𝗰 𝗦𝗲𝗺𝗮𝗻𝘁𝗶𝗰 𝗟𝗶𝗻𝗸

Ever updated a templated Fabric solution (like the Fabric Unified Admin Monitoring (FUAM)), only to realize your custom security setup was overwritten? 😬

That’s exactly what could happen after each update! But of course, you don't want to manually reconfigure roles, users, and filters all over again. A manual, error-prone, and time-consuming process.

So… why not automate it? 💡
In my latest blog, I show how you can script and deploy your security configurations directly to your semantic models using Fabric Semantic Link. From defining roles and assigning members, to setting up RLS expressions, all in a reusable, parameterized Fabric notebook.

👉 Read the full walkthrough and grab the sample notebook from my GitHub:
 🔗 https://lnkd.in/er3pvbvu
#MicrosoftFabric #PowerBI #SemanticLink #DataGovernance #Automation #FabricCommunity

---

## [How Microsoft Fabric ensures business continuity with BCDR](https://www.linkedin.com/feed/update/urn:li:activity:7386852341829795840?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7386852341829795840%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** Building Resilience with Microsoft Fabric: Business Continuity and Disaster Recovery (BCDR) Simplified

In Financial Services and other mission-critical industries, analytics and AI cannot afford downtime. Microsoft Fabric’s end-to-end BCDR framework ensures operational continuity, even in the face of regional outages or disasters.

Here’s how Fabric BCDR transforms resilience:

- Automated Geo-Replication: OneLake data is asynchronously mirrored across Azure paired regions for durability and compliance.
- Artifact Versioning: Git-integrated pipelines, notebooks, and semantic models can be instantly reconstructed post-failover.
- Orchestrated Recovery: Fabric automates failover provisioning, workspace recreation, and integrity validation within an RTO and RPO based on business requirements and application.
- Real-time Monitoring: Replication health, lag, and cost metrics are surfaced natively in Fabric Capacity Metrics.
- Regulatory Confidence: BCDR meets stringent FSI continuity mandates with full audit trails and DR-drill documentation.

In a world where data is the new gold, continuity is the new currency. 

#MicrosoftFabric #BCDR #DataEngineering #Azure #Resilience #OneLake #AI #Analytics 

---

## [Integrating Azure AI Foundry with Microsoft Fabric](https://jehayesms.github.io/jean-hayes-ai-analytics/azure%20ai/microsoft%20fabric/2025/10/21/integrating-azure-ai-with-fabric.html)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** The article shows how to call an Azure AI Foundry Content Understanding endpoint from a Microsoft Fabric notebook to extract data from complex documents and save results to a Fabric Lakehouse. It explains storing secrets in Azure Key Vault, using managed private endpoints, and building reusable pipelines and variable libraries. Finally, it describes publishing a Fabric Data Agent for Q&A and using it with Power BI Copilot and other apps.

---

## [Fabric Spark best practices overview - Microsoft Fabric](https://learn.microsoft.com/en-us/fabric/data-engineering/spark-best-practices-overview)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** This series gives best practices for running Spark Notebooks and Spark Job Definitions on Microsoft Fabric. It covers performance, security, and cost optimization. New users should read the Spark Basics and Fabric data engineering docs first.

---

## [Authenticate as a service principal to run a Microsoft Fabric notebook from Azure DevOps](https://www.kevinrchant.com/2025/01/31/authenticate-as-a-service-principal-to-run-a-microsoft-fabric-notebook-from-azure-devops/)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** The post shows how to authenticate as a service principal to run Microsoft Fabric notebooks from Azure DevOps using the REST API. It explains three pipeline tasks: get the notebook ID, start the notebook run, and poll run status, with PowerShell examples. The author tests both successful and failing runs and highlights that service principal support is now available.

---

## [Automating Power BI Data Quality Checks with Great Expectations & SemPy](https://www.linkedin.com/pulse/automating-power-bi-data-quality-checks-great-sempy-muhammad-samy-nnv8e?utm_source=share&utm_medium=member_ios&utm_campaign=share_via)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** Data models and data quality are never simple in the enterprise. Our Power BI semantic models combine large fact tables, multiple aggregates, and complex refresh logic.

---

## [Understand Direct Lake query performance - Microsoft Fabric](https://learn.microsoft.com/en-us/fabric/fundamentals/direct-lake-understand-storage)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** Learn how Direct Lake query performance depends on Delta table health and efficient data updates. Understand the importance of V-Order optimization, row groups, and Delta log management for optimal query execution.

---

## [Tom Baeyens’ Post](https://www.linkedin.com/feed/update/urn:li:activity:7388540392268464128?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7388540392268464128%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** Data contracts is Governance packaged as Data Engineering.

Traditional governance has struggled in data teams.

Policies are often written in documents that engineers rarely read, and enforcement depends on manual reviews.

Data engineers always see it as extra paper work.

Data contract is a formal agreement that specifies the schema, semantics, and expectations from a dataset. It defines what fields exist, their data types, update frequency, and quality thresholds. This is governance.

It is enforced through code. It validates data deployment, and monitors production datasets. This is engineering.

Leaders get direct value on building contracts is because they close the gap between policy and implementation.

Producers and consumers operate on the same definition of what good data means.

Manual governance would simply never scale the way data contracts do.

Learn more here: https://lnkd.in/g8GMWCUf | 22 comments on LinkedIn

---

## [Luis Lopez-Pons’ Post](https://www.linkedin.com/feed/update/urn:li:activity:7389571801959518208?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7389571801959518208%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** 💰 You don't have budget for #AzureDatabricks, #AzureSynapse or a big #MicrosoftFabric Capacity?
Turns out, you might not need them.
If you're small, you can replace an average analytics stack with #AzureFunctions + DuckDB.

📊 Case: 8-minute daily pipeline that costs $3/month.
No Databricks. No Synapse. No always-on databases.
—
🛠️ The Stack:
→ ⚡ Azure Functions (Consumption Plan) → 🦆 DuckDB embedded in Python → 📦 Parquet files on Blob Storage → 📈 Power BI for visualization
—
⚙️ The Flow:
⏰ Timer trigger fires at night
📂 DuckDB reads Parquet directly from Blob Storage (no copying!)
🧠 SQL transformations run in-memory
💾 Results written back as Parquet
📊 Power BI queries the output
—
✨ Why This Actually Works:
DuckDB has native Azure Blob support. It queries #Parquet at 1GB/second per core. No infrastructure to manage. No state between runs.
The same SQL that runs in production runs on your laptop with sample data.
—
📈 Real Performance Numbers:
5GB of order data
Complex joins + aggregations
⏱️ 2.5 minutes on a single Azure Function
💵 $3/month total cost
—
💡 The Insight:
Enterprise data tools are amazing, but there’s no one-size-fits-all solution.
If you're processing GB (not TB), running batch analytics (not real-time), and need OLAP (not OLTP), you might be over-engineering.
Sometimes a $3 solution beats a $3,000 solution.
—
🎯 Who is this for?
✓ 🚀 Startups watching every euro ✓ 👥 Small data teams without platform engineers ✓ 📁 Companies with data in files already ✓ 😤 Anyone tired of infrastructure overhead

Is your data stack simpler or more complex than it needs to be? 💭

#DataEngineering #Azure #DuckDB #CostOptimization #Serverless #AzureFunctions #DataAnalytics #BatchAnalytics | 11 comments on LinkedIn

---

## [Microsoft Fabric supports Managed Private Endpoints for secure data access](https://www.linkedin.com/feed/update/urn:li:activity:7388681278327410688?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7388681278327410688%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** Microsoft Fabric now supports Managed Private Endpoints—enabling secure, governed connectivity from Spark workloads to on-premises and network-isolated data sources.

What it enables:  
- Establish private connectivity from Fabric workspaces to SQL Server, ADLS, and other restricted resources  
- Avoid public internet exposure by allowlisting Fully Qualified Domain Names (FQDNs) via Private Link Service  
- Trigger admin approval workflows for endpoint creation and governance  
- Use native Spark engine for high-performance processing on secured datasets  
- Configure and monitor connections via Fabric Public REST APIs

Why it matters:  
- Eliminates need for VPNs or gateways in hybrid architectures  
- Strengthens enterprise security posture with domain-level access control  
- Simplifies ingestion and analytics across regulated environments  
- Enables scalable, compliant data engineering workflows

How to get started:  
- Identify your Private Link Service resource ID  
- Create a Managed Private Endpoint using Fabric APIs  
- Add target FQDNs and request admin approval  
- Verify domain mappings and begin Spark-based processing

Details on the blog: https://lnkd.in/gy98xECs 

#MicrosoftFabric #PrivateLink #ManagedPrivateEndpoint #MSFTAdvocate


---

## [Sandeep Pawar’s Post](https://www.linkedin.com/feed/update/urn:li:activity:7394508585407483904?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7394508585407483904%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** If you want to learn how #DataAgent in #MicrosoftFabric work and need a hands-on, step-by-step guide, my colleagues Markus Cozowicz Shreyas C. have an awesome repo. Be sure to give it a ⭐.

More coming soon...

📌https://lnkd.in/gMWgyWtj
📌https://lnkd.in/gDQv8zMy

---

## [Achraf C.’s Post](https://www.linkedin.com/feed/update/urn:li:activity:7394972973805355009?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7394972973805355009%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** 🎉🎉 The Onelake duckdb extension is now available as a community extension: https://lnkd.in/eWbW823Q

Current functionalities :
✅ Authentication via azure CLI, managed identity and Fabric workspace identity.
✅ Attach to any Lakehouse 
✅ Use the Lakehouse schemas as DuckDB schemas 
✅ Read Delta and Iceberg tables

Thanks Mimoune Djouallah for the feature ideas,  Sam Ansmink and Carlo Piovesan for the quick help in getting the extension merged. | 13 comments on LinkedIn

---

## [Kafka + DuckDB benchmarks: 50M messages in 11.62s](https://www.linkedin.com/feed/update/urn:li:activity:7397140898951614464?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7397140898951614464%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** I've been deep in 𝗞𝗮𝗳𝗸𝗮 + 𝗗𝘂𝗰𝗸𝗗𝗕 development the past few weeks, but here are some late-night benchmarks from my couch 🛋️:

🆕 Created a Kafka topic with 8 partitions on my M3 MacBook Air (one per core)
⚡ Inserted 50M messages from DuckDB (47 bytes each) in 11.62s (𝟰.𝟯 𝗺𝗶𝗹𝗹𝗶𝗼𝗻 𝗺𝘀𝗴𝘀/𝘀𝗲𝗰)
👀 Scanned those messages directly from Kafka in DuckDB in 17.54s (𝟮.𝟴𝟱 𝗺𝗶𝗹𝗹𝗶𝗼𝗻 𝗺𝘀𝗴𝘀/𝘀𝗲𝗰)
🐤 Inserted them into a local DuckDB table in 29.63s (𝟭.𝟲𝟵 𝗺𝗶𝗹𝗹𝗶𝗼𝗻 𝗺𝘀𝗴𝘀/𝘀𝗲𝗰)

More CPU cores and more Kafka partitions make it even faster.

A lot of this speed comes from DuckDB's ability to facilitate zero-data-copy with the Kafka client library — no need to copy messages around instead just attach them to DuckDB vectors as auxiliary data.

🐤 𝗗𝘂𝗰𝗸𝗗𝗕 + 𝗞𝗮𝗳𝗸𝗮 𝗶𝘀 𝗳𝗮𝘀𝘁 🚀 — 𝗮𝗻𝗱 𝘁𝗵𝗶𝘀 𝗶𝘀 𝗷𝘂𝘀𝘁 𝘁𝗵𝗲 𝗯𝗲𝗴𝗶𝗻𝗻𝗶𝗻𝗴!

Next up: benchmarking Avro, Protobuf, and JSON Schema registry support. The code is written — it's been quite the adventure.

𝗧𝗵𝗶𝘀 𝘄𝗶𝗹𝗹 𝗯𝗲 𝗤𝘂𝗲𝗿𝘆.𝗙𝗮𝗿𝗺'𝘀 𝗳𝗶𝗿𝘀𝘁 𝗰𝗼𝗺𝗺𝗲𝗿𝗰𝗶𝗮𝗹𝗹𝘆 𝗹𝗶𝗰𝗲𝗻𝘀𝗲𝗱 𝗗𝘂𝗰𝗸𝗗𝗕 𝗲𝘅𝘁𝗲𝗻𝘀𝗶𝗼𝗻. The new website is launching soon.  

https://query.farm - Meet with us to get a demo.

#DuckDB #Kafka #DuckDBExtension #Tributary #Streaming #SQL #StreamingSQL #MaterializedViews | 35 comments on LinkedIn

---

## [David Kofod Hanna’s Post](https://www.linkedin.com/feed/update/urn:li:activity:7400058406385938434?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7400058406385938434%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** Is it just hype?
Can't we just script it?
How to get started with Power BI Modeling MCP Server?
What does it cost?
Can't I just use Tabular Editor?
What is MCP?
Do we need source control?

I have tried to break it down for you in this article

Enjoy and have fun ✨ | 18 comments on LinkedIn

---

## [Dennes Torres’ Post](https://www.linkedin.com/feed/update/urn:li:activity:7401014851252170752?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7401014851252170752%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** 🔥🔥🔥 Fabric Monday Highlights: Translytical Taskflow 🔥🔥🔥

In this playlist, I showcase the Translytical TaskFlow architecture in Microsoft Fabric using a simple example: a system to capture annotations over the data and save them directly in Fabric.

But that’s just one way to use it. This architecture lets you connect user interactions directly to the platform, enabling actions like:

🆕 Refresh the semantic model from a report — a long-awaited capability
 🎯 Adjust KPI targets dynamically
 ⚡ …and many other data-driven operations

Translytical TaskFlows make it possible to turn insights into actions instantly, without leaving the Fabric environment.

🔗 Link of the playlist in the comments

Curious: which scenario would you use it for first?

👉 Fabric Monday 75: What's Translytical Taskflow

👉 Fabric Monday 76: Creating User Data Functions

---

## [Dennes Torres’ Post](https://www.linkedin.com/feed/update/urn:li:activity:7399332605269102592?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7399332605269102592%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** 🎬✨ Mastering Shortcuts in Fabric

Ever felt like your Fabric workspace has shortcuts that… mysteriously stop working?

 
Or worse — shortcuts pointing to things that don’t even exist anymore?
In this video I walk through a simple way to stay in control of your shortcut ecosystem.

✨ Here’s what you’ll find inside:
👉 How to quickly surface shortcuts that need attention
 👉 A practical trick to spot broken ones using code
 👉 And a small insight that can save you from hours of guesswork

If shortcuts are part of your daily flow, this one will make your life much easier.

---

## [Sandeep Pawar’s Post](https://www.linkedin.com/feed/update/urn:li:activity:7404193477921529859?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7404193477921529859%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** 💡Did you know you can programmatically test, validate and improve your #MicrosoftFabric #DataAgent using a Python SDK? You can do that in Fabric notebook or use the external client in any IDE outside of Fabric too !  You can also inspect the diagnostic log to identify if you need to improve the instructions, add/tune few-shots etc...

📑Docs: https://lnkd.in/giCFUpHW

🛠️Eval Notebooks : https://lnkd.in/d3juqS97

📌External client : https://lnkd.in/gTMWdBu6

👉Follow these best practices : https://lnkd.in/gNy6u58Z

Give it a try and if you have any feedback, send it my way.

---

## [Diego Nolleau’s Post](https://www.linkedin.com/feed/update/urn:li:activity:7405306370906038272?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7405306370906038272%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** 🚀 Nouvelle fonctionnalité Power BI (mise à jour de novembre) : intégration d’un serveur MCP (Model Context Protocol)

Qu’est-ce qu’un MCP ?

Il s’agit d’un protocole standard qui permet à un modèle d’IA de se connecter de manière sécurisée et structurée à des outils et à des sources de données externes, comme Power BI.

👉 Concrètement, cela permet d’interagir avec votre modèle Power BI en langage naturel et même de modifier sa structure via l’IA.

✅ Comment l’utiliser avec Power BI :

1. Télécharger VS Code  
2. Installer les extensions suivantes :
   - GitHub Chat  
   - GitHub Copilot  
   - Power BI MCP Server  
3. Ouvrir votre rapport Power BI Desktop  
4. Sur VS Code, lancer une conversation avec l’IA en mode « Agent » en activant le MCP dans les outils (pour accéder aux outils, cliquez sur l’icône présente dans la 4ème capture d’écran à droite de « Claude Haïku »
5. Créer la connexion en écrivant :
   "Connect to '[File Name]' in Power BI Desktop"
6. Une fois connecté, utiliser l’agent IA pour :
   - créer des mesures
   - créer des colonnes calculées
   - créer des tables
   - modifier le modèle

On passe d’un travail purement technique (DAX / modélisation) à une interaction directe en langage naturel avec son modèle de données.

🚨 Cette fonctionnalité est en préversion, faites un doublon de votre fichier avant de commencer à tester ses capacités afin d’éviter les mauvaises surprises 😉

#PowerBI #Data #IA

---

## [Charlotte Ledoux’s Post](https://www.linkedin.com/feed/update/urn:li:activity:7405883010614476800?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7405883010614476800%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** Despite everything we hope AI will assist and automate, no technology alone will populate and maintain the catalog.

Roles that matter :

👔 Data Owner (business): accountable for definitions, SLAs and business acceptance. This is the person who signs off when the glossary term changes.

🧑‍🔧 Data Steward (domain): maintains metadata, manages reviews, and orchestrates fixes with producers. Stewards also mediate disputes about definitions or quality.

⚙️ Data Producer (engineering): implements schema changes, publishes lineage and raises change requests into the catalog pipeline.

🔍 Data Consumer (analyst/product): provides feedback, reports issues, and validates the catalog entries against business use.

Read more in the article by Peter Baumann explaining how to get value from metadata thanks to a Data Catalog :

https://lnkd.in/dW3FHV_w | 14 comments on LinkedIn

---

## [How to build an AI agent in Fabric and Foundry to leverage your business data](https://www.linkedin.com/feed/update/urn:li:activity:7404865390285332480?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7404865390285332480%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** If you have been waiting for a step‑by‑step tutorial to make an AI agent that “speaks” the language of your business data, this guide is for you. In this article I will show you how to: (1) build a Fabric Data Agent over your Fabric Lakehouse and (2) connect that agent to Microsoft Foundry to enable extended agent capabilities.

If you have any questions, please feel free to contact me! 

#Fabric, #FabricDataAgent, #Foundry, #PwC

---

## [Microsoft Fabric IQ: Solving Ontology Issues for AI-Ready Data](https://www.linkedin.com/feed/update/urn:li:activity:7404845109827174400?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7404845109827174400%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** “Most organisations don’t struggle with AI readiness because of tools… they struggle because their data has no shared language.”

Over the past year, I’ve spoken with CIOs, CDOs, and Data Leaders across the GCC and Europe and the pattern is the same every time.

Teams are investing heavily in Microsoft Fabric, AI Agents, and LLMs…
but relationships across the data estate are still fragmented.

And without shared meaning —
AI can’t reason, predict, or trust your data.

Here’s what leaders tell me repeatedly:

“Our semantic models don’t scale across domains.”

“AI gives inconsistent answers because context isn’t unified.”

“We can’t connect real-time and historical data cleanly.”

“Everything feels fast… but not aligned.”

It’s never a tooling issue.
It’s an ontology issue — a clarity issue.

That’s why I created this cheatsheet for Fabric IQ, Microsoft’s ontology layer for AI-ready data.
Because when organisations shift from tables to entities + relationships, everything changes:

AI Agents reason with business context
Cross-domain data becomes unified
Real-time + historical insights become consistent
Governance improves automatically
Your Microsoft Fabric estate becomes “AI-ready” instead of “AI-hopeful”

This is the difference between
AI that answers and AI you can actually trust.

If you want to understand how to apply Fabric IQ to your own Microsoft estate — and avoid the common mistakes that break AI outcomes I’ve opened a few early access slots this week.

📌 Comment “FABRIC IQ” below
and I’ll share the full implementation framework we use with clients across UAE, KSA, Qatar & Europe, including governance, design steps, and real case examples.

Because AI success doesn’t start with models.
It starts with meaning.

— Leon Gordon
Microsoft MVP

#MicrosoftFabric #DataGovernance #AIReadyData #Ontology #FabricIQ #EnterpriseAI #MicrosoftPartner | 91 comments on LinkedIn

---

## [Adrian Chodkowski’s Post](https://www.linkedin.com/posts/adriansql_microsoftfabric-deltalake-spark-activity-7406230293411631104-HYJ1?utm_source=share&utm_medium=member_ios&rcm=ACoAAA4TApsBpcD7dMto9tdEqMhSTfRhiYAy83E)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** Did you know that neglecting Delta table maintenance in many Fabric implementations leads to excessive costs and degraded performance?

Manual tuning of target file sizes can be complex, but Microsoft Fabric simplifies this with Adaptive Target File Size - a smart feature that automatically estimates and adjusts the ideal Parquet file size based on table heuristics, eliminating the need for ongoing manual intervention.

Key benefits:
• Starts at 128 MB for small tables (<10 GB) and scales linearly up to 1 GB for tables >10 TB
• Enhances Delta file skipping
• Reduces costs for MERGE/UPDATE operations
• Optimizes Spark task parallelism for better read/write throughput
• Can improve compaction performance sometimes by 30–60%

Enable it easily in your Spark session:
SET spark.microsoft.delta.targetFileSize.adaptive.enabled = TRUE

It auto-evaluates during CTAS, overwrites, new table creates, and every OPTIMIZE command. Override when needed with the explicit delta.targetFileSize property.
Highly recommended, especially as your data grows!

#MicrosoftFabric #DeltaLake #Spark #DataEngineering #Lakehouse

---

## [SQL Telemetry & Intelligence – How we built a Petabyte-scale Data Platform with Fabric](https://blog.fabric.microsoft.com/en-us/blog/sql-telemetry-intelligence-how-we-built-a-petabyte-scale-data-platform-with-fabric?ft=All)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** Microsoft Fabric built a huge data platform using tools like OpenTelemetry, Azure Data Explorer, and Spark Streaming to handle petabytes of data quickly and reliably. They use smart data models like Kimball SCD2 and DirectLake for accuracy and fast queries. Developers work easily with a special VSCode setup that matches the platform’s complex environment.

---

## [Explaining the 10, 60 and 1440 minute throttling limits- Part 1: What is throttling and how do I identify it?](https://www.linkedin.com/pulse/explaining-10-60-1440-minute-throttling-limits-part-1-matthew-farrow-z1kse?utm_source=share&utm_medium=member_ios&utm_campaign=share_via)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** In this three-part article series, I will look at how throttling is applied in Fabric capacities. A while ago I wrote this article, which explained smoothing; with this series, I aim to expand the explanation with a new analogy, illustrated by practical examples.

---

## [Sandeep Pawar’s Post](https://www.linkedin.com/feed/update/urn:li:activity:7411896510067576832?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7411896510067576832%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** 📢#MicrosoftFabric #DataAgent ending the year with a bang 💥

Data Agent MCP server is now available !!! You can add the MCP server to VS Code (or an external app) and interact with the data. Be sure to provide a clear and comprehensive description of the agent when publishing to invoke the right agent as a tool.

Congratulations to the team !!! 

✨2026 is going to be the year of Data Agent, more to come.

📌Docs: https://lnkd.in/gYcKAYkJ

As always, if you have feedback let us know. | 11 comments on LinkedIn

---

## [Optimizing Delta Tables in the Silver Layer](https://chasinginsights.com/optimizing-delta-tables-in-the-silver-layer)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** Congrats you’ve built your first medallion architecture. Good news is you’ve finally gotten through all the business lines of questions, validation, and intense engineering workloads. The issue is now your processes are slowly getting slower and slow...

---

## [Christopher Schmidt’s Post](https://www.linkedin.com/feed/update/urn:li:activity:7415014501579890690?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7415014501579890690%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** Over the past few months, I’ve spent a lot of time thinking about a deceptively simple question:

How do architectural choices for real-time ingestion in Microsoft Fabric actually impact CU consumption and latency?

This edition of the #realtimedispatch is the result of finally taking the time to test that question in a structured, data-driven way.

Using the NYC Yellow Taxi dataset (May 2025), I evaluated two common real-time ingestion architectures in Fabric:

Event Hub → #Eventstream → Eventhouse (RTI)
Event Hub → #SparkStructuredStreaming → Silver Table

The goal was not to declare a universal “winner,” but to provide an objective comparison of:
CU consumption behavior over time
End-to-end latency
How each approach scales as volume increases
What these patterns imply for real-world capacity planning
To keep the results realistic, all data was generated externally (outside Fabric), transformations were applied in flight, and measurements were scoped strictly to ingestion and transformation costs.

What this edition covers:
How RTI services (Eventstream + Eventhouse) consume CU in a steady, pay-as-you-go pattern
Why Spark Structured Streaming can appear efficient at low volume but becomes increasingly expensive and bursty at scale
How notebook CU consumption is time-bucketed, and why that can distort perceived cost
Why volume (bytes), not row count, is the key driver for RTI CU usage
Practical guidance for forecasting Fabric capacity as streaming workloads grow
Key takeaway
As streaming volume increases, architectural decisions matter more than tooling familiarity. RTI workloads in Fabric scale more predictably and cost-effectively with volume, while Spark-based approaches can introduce CU spikes, back-pressure, and throttling at higher throughput.
If you are designing or operating real-time ingestion pipelines in Fabric—or trying to forecast capacity before going to production—this edition is intended to give you concrete data points to support those decisions...

---

## [Vibe Optimizing Power BI](https://www.linkedin.com/feed/update/urn:li:activity:7415037672424935424?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7415037672424935424%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** 🚀 Vibe Optimizing Power BI – Are Your Report and Model Fast Enough and optimized?

Slow Reports kill the vibe. Discover how to boost performance & user experience with a new tool from Microsoft Fabric Toolbox: DAX Performance Tuner MCP Server.
✅ Real-world demo
✅ Before/After optimization
✅ Tips for tuning your Power BI reports

👉 Read the full article and see how MCP can transform your Report

#PowerBI #MicrosoftFabric #DAXOptimization #FinOps #DataAnalytics

---

## [Charlotte Ledoux’s Post](https://www.linkedin.com/feed/update/urn:li:activity:7416029860445249536?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7416029860445249536%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** 🟡 Metadata is the common language for all teams.

Metadata is not a technical layer, but context that travels with data. 
It connects meaning across systems, teams, and repositories.

We need a shared understanding of business processes and pains across units and departments. Everyone, from data engineers to business leaders, should start using the same words to describe the same things : domain, owner, data product, and source.

Thank you Gaëlle SERET for this great article !

https://lnkd.in/dEnQBMiB | 14 comments on LinkedIn

---

## [Microsoft Purview Unified Catalog: Deploys in Minutes, Transform in Years (And Why That’s Actually Good News)](https://medium.com/@marcoOesterlin/microsoft-purview-unified-catalog-deploys-in-minutes-transform-in-years-and-why-thats-actually-512a5567e629)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** Microsoft Purview deploys in minutes. A few clicks in the Azure & Microsoft Purview portal, some resource configurations, a deployment…

---

## [Developing with OneLake on Desktop and Deploying to Microsoft Fabric](https://www.linkedin.com/feed/update/urn:li:activity:7416849920692793344?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7416849920692793344%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** Sharing my own workflow in the hope it may be useful: how I develop locally on my desktop and deploy to #MicrosoftFabric using #VSCode, #Copilot, and #PowerBI #Desktop.

The key idea is that OneLake can be accessed from anywhere.

Business logic should ideally live in SQL and Python scripts, not be embedded in notebooks. Notebooks are great for orchestration and exploration, but they should stay thin.

Always use ABFSS paths and avoid coupling your Lakehouse to a specific notebook. This keeps your architecture portable and easier to move to other workspace

AI is changing our daily workflow and that's great !!

#DuckDB #DeltaTable #sql #python #duckdb #polars #onelake 

https://lnkd.in/gz-QFEMk

---

## [Jean Hayes’ Post](https://www.linkedin.com/feed/update/urn:li:activity:7416886178336944128?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7416886178336944128%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** Happy New Year Everybody!
Over the past year, I’ve helped many customers optimize their Microsoft Fabric environments—and surprisingly, a large number of issues came down to capacity and workspace design. Noisy neighbors, throttling, scaling up vs. scaling out… you name it.
To help you get ahead of these challenges, I wrote an article on capacity and workspace design:  https://lnkd.in/gYB9JQ4x 

I’ve also included a downloadable Fabric Capacity & Workspace Discovery process to help you design the optimal environment that fits your organization’s needs. I hope you find it valuable!

Special thanks to Holly Kelly for all the work she has done in this space! 

#microsoftfabric #fabric #FSKU #Microsoft #workspace #capacity #optimization

---

## [Yassine Mahboub’s Post](https://www.linkedin.com/feed/update/urn:li:activity:7415362145007304704?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7415362145007304704%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** 📌 How to Gather Dashboard Requirements

(Requirements Gathering 101)

The success of a Data or BI project doesn’t start with the tool you pick or the stack you deploy.

It starts earlier.

It starts with something less exciting, but far more important: gathering clear business requirements.

And yet, this is the step that gets skipped the most.

Everyone wants to talk about architecture, pipelines, medallion layers, AI copilots…

But if you don’t know what the business actually needs, none of that matters.

So what does "gathering requirements" actually look like?

It means sitting down with stakeholders and asking questions that sound simple on the surface, but change everything:

⤷ What decisions are you struggling to make today?
⤷ Where does data slow you down or create confusion?
⤷ Which KPIs, if you had them right now, would change how you run the business?

These conversations are rarely neat.

You’ll hear conflicting priorities, vague goals, and sometimes even silence.

That’s normal. The job is to cut through the noise and translate it into something concrete.

When you do that, everything else falls into place:

1) Data engineers know exactly which sources to prioritize.

2) Data Analysts stop debating vanity metrics and focus on useful KPIs.

3) Leaders understand what to expect once dashboards go live.

And here’s what often gets overlooked: requirement gathering isn’t just about listing KPIs.

It’s here to map business decisions to data, spot workflow bottlenecks, align with strategy, and create a shared language across business and technical teams.

It’s where you discover that the sales team and the finance team define "revenue" differently.

It’s where you realize that a monthly report isn’t enough, and what the business really needs is daily visibility.

It’s where you uncover that the pain point isn’t the dashboard at all, but the manual process feeding it.

Data platforms and BI tools will keep changing.

Snowflake, Databricks, Fabric, Big Query...

---

## [Yassine Mahboub’s Post](https://www.linkedin.com/feed/update/urn:li:activity:7417172841214947328?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7417172841214947328%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** 📌 MS Fabric Breakdown # 15: User Data Functions

One of my favorite features released last year in Fabric is User Data Functions (UDFs).

Think of it like an Azure Function built directly into Fabric. It allows you to host and run your own custom code that can be used by different workloads across your data platform.

To put it simply: UDFs allow you to bring your own "serverless" logic to Fabric.

And there are massive benefits to this approach:

1️⃣ 𝐑𝐞𝐚𝐝𝐚𝐛𝐢𝐥𝐢𝐭𝐲

Build a function once and reuse it across 50+ notebooks or pipelines without duplicating code.

2️⃣ 𝐂𝐮𝐬𝐭𝐨𝐦𝐢𝐳𝐚𝐭𝐢𝐨𝐧

It’s just Python so you have the freedom to build whatever complex logic you need without being restricted by standard low-code activities.

3️⃣ 𝐖𝐨𝐫𝐤𝐟𝐥𝐨𝐰 𝐒𝐢𝐦𝐩𝐥𝐢𝐟𝐢𝐜𝐚𝐭𝐢𝐨𝐧

You can encapsulate complex logic that would normally require a lot of Logic Apps or Power Automate flows.

4️⃣ 𝐑𝐄𝐒𝐓 𝐄𝐧𝐝𝐩𝐨𝐢𝐧𝐭

You can invoke your functions from external applications and simplify your integration strategy.

This opens up a world of use cases when working with Data Factory or Notebooks and I’ve found some patterns very useful like:

→ Custom pre/post-processing logic for pipelines
→ Notification utilities (Slack, Teams, email formatting)
→ Metadata-driven routing and branching logic
→ Reusable enrichment or normalization functions

In the featured screenshot for example, I built a Slack notification function with advanced formatting for pipeline runs.

It’s a simple workflow but you can take it much further like adding intelligent error summaries and generating debugging hints

You can even plug in LLM APIs (ex: Claude or Gemini) to suggest root causes or next steps directly in the notification.

One thing to keep in mind though is that UDF connections are limited to Fabric’s internal items (Lakehouse, SQL Database, etc.).

External connectivity is still constrained but hopefully this expands over time. External APIs are a great alternative for this.

Still, if you’re building serious solutions in Fabric, U...

---

## [Harsha Guggilla’s Post](https://www.linkedin.com/feed/update/urn:li:activity:7417958824764076032?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7417958824764076032%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** Optimize Write in Microsoft Fabric Spark 

In the previous posts, we talked about table Delta table layout(file count + file sizes + partition shape) and we discussed that this layout matters because Spark has to plan work and reason about metadata before it can touch our data.
 
So when teams ask “why did this table got slower even though my query did not change?” most often the answer is because the spark writes kept producing small files and so the table layout kept getting more fragmented and that’s why planning and maintenance costs unfortunately creep up over time.

Now here the important thing is:
Even if we have a good target file size in mind, we still need a mechanism that influences what happens during the write, because if our pipeline keeps emitting lots of tiny output files, then we are basically creating future OPTIMIZE / compaction work for ourselves. And that is exactly what Optimize Write is designed to reduce.

What Optimize Write actually does
Microsoft describes Optimize Write as pre-write compaction (bin packing), because it means that Spark tries to bundle in-memory data into optimally sized bins before writing Parquet files, so you get fewer, larger files without needing immediate post-write cleanup. 

And because that bin packing often requires shuffling data, so it can add some compute cost, but it can still be a win because it is often cheaper to avoid creating thousands of tiny files than it is to rewrite them later via post-write compaction.

Why to use it for partitioned tables
Optimize Write is normally super useful for partitioned tables and the reason is when we write into partitions, multiple tasks can end up writing separate output files into the same partition path and so file counts per partition can explode quickly, especially with micro-batches. 

But it can still matter for non-partitioned tables, because small files can also happen there if you write with a lot of parallelism..So, it "might be" beneficial when the write wo...

---

## [LinkedIn](https://www.linkedin.com/feed/update/urn:li:activity:7419123680607105024?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7419123680607105024%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** 500 million+ members | Manage your professional identity. Build and engage with your professional network. Access knowledge, insights and opportunities.

---

## [Stefano Pescosolido’s Post](https://www.linkedin.com/feed/update/urn:li:activity:7419112140818796544?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7419112140818796544%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** A new technology doesn’t really exist until 𝘑𝘰𝘩𝘯 has explained it — at least in my opinion... 😅 
🎥 𝐃𝐞𝐞𝐩 𝐃𝐢𝐯𝐞 𝐢𝐧𝐭𝐨 𝐅𝐨𝐮𝐧𝐝𝐫𝐲 𝐈𝐐: https://lnkd.in/dPYUDZgE

#MicrosoftFoundry 
John Savill

---

## [Vladimir Gribanov’s Post](https://www.linkedin.com/feed/update/urn:li:activity:7423810643738128384?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7423810643738128384%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** Vladimir Gribanov released a new DuckDB extension for fast, direct data loading into SQL Server without ODBC. It supports full data operations and can load over a million rows per second. This tool improves performance and simplifies data engineering.

---

## [https://www.linkedin.com/feed/update/urn:li:article:7789579232378486340?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aarticle%3A7789579232378486340%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29](https://www.linkedin.com/feed/update/urn:li:article:7789579232378486340?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aarticle%3A7789579232378486340%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** Summary not available.

---

## [https://www.linkedin.com/feed/update/urn:li:article:9128354385763810451?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aarticle%3A9128354385763810451%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29](https://www.linkedin.com/feed/update/urn:li:article:9128354385763810451?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aarticle%3A9128354385763810451%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** Summary not available.

---

## [https://www.linkedin.com/feed/update/urn:li:article:8057127566142043336?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aarticle%3A8057127566142043336%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29](https://www.linkedin.com/feed/update/urn:li:article:8057127566142043336?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aarticle%3A8057127566142043336%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** Summary not available.

---

## [Vladimir Gribanov’s Post](https://www.linkedin.com/feed/update/urn:li:activity:7426339156487901185?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7426339156487901185%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** Vladimir Gribanov announced a new DuckDB extension for Azure SQL and Microsoft Fabric with improved authentication and faster metadata loading. Azure SQL migration tools are being updated or deprecated, with new guidance provided for smooth transitions. Dell Technologies and Azure Stack aim to simplify hybrid cloud SQL Server management for better performance and control.

---

## [Tabular Editor’s Post](https://www.linkedin.com/feed/update/urn:li:activity:7426931484218961920?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7426931484218961920%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** Power BI and Fabric models can save memory by using the VertiPaq Analyzer to find and fix heavy data. Large language models train faster and better by processing data in batches instead of one word at a time. Techniques like Support Vector Machines and memory-efficient backpropagation improve machine learning performance and reduce resource use.

---

## [Piotr Czarnas’ Post](https://www.linkedin.com/posts/piotr-czarnas_dataquality-dataengineering-datagovernance-activity-7432056440707686400-EOJx?utm_source=share&utm_medium=member_ios&rcm=ACoAAA4TApsBpcD7dMto9tdEqMhSTfRhiYAy83E)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** Data Fabric is an architecture that simplifies data access by hiding integration complexity. It combines real-time access, automation, and governance to ensure data quality and freshness. True Data Fabric helps users trust their data by managing metadata and tracking data usage centrally.

---

## [Dr. Simon Harrer’s Post](https://www.linkedin.com/posts/simonharrer_datacontracts-datamodeling-datamesh-activity-7432758649514692609-bTyf?utm_source=share&utm_medium=member_ios&rcm=ACoAAA4TApsBpcD7dMto9tdEqMhSTfRhiYAy83E)
📅 2026-02-27 · 🌐 Reader Share Sheet iOS

**Summary:** The Data Contract Editor turns data models into full agreements between data producers and consumers, adding rules, ownership, SLAs, and access control. It uses a single YAML file based on an open standard and automates quality checks in CI/CD pipelines. The tool is open source, customizable, and easy to run in a browser, CLI, or Docker.

---

## [Yassine Mahboub’s Post](https://www.linkedin.com/feed/update/urn:li:activity:7427683086869606400?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7427683086869606400%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29)
📅 2026-02-26 · 🌐 Reader Share Sheet iOS

**Summary:** Good data quality is the foundation for trustworthy business insights and AI. Teams must focus on accuracy, checks, and strong governance to build data trust. Without trust, decisions and AI results become unreliable.

---

## [Mimoune Djouallah’s Post](https://www.linkedin.com/feed/update/urn:li:activity:7428408152313987072?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7428408152313987072%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29)
📅 2026-02-26 · 🌐 Reader Share Sheet iOS

**Summary:** Mimoune Djouallah explains how to use Microsoft Fabric’s SQL Endpoint to read secured OneLake tables from external tools like DuckDB. DuckDB supports many data sources, making it a powerful data virtualization layer. This approach helps maintain data security while enabling easy data access and analysis.

---

## [Optimize Delta Table Performance with Deletion Vectors](https://www.linkedin.com/feed/update/urn:li:activity:7427757216922947584?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7427757216922947584%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29)
📅 2026-02-26 · 🌐 Reader Share Sheet iOS

**Summary:** Deletion Vectors in Delta tables let you delete or update millions of rows without rewriting large files, improving performance. Delta uses Parquet files with metadata to enable fast, efficient reads and updates. Choosing the right file format and optimizing queries greatly speeds up data processing in Databricks.

---

## [Automating Engineering Workflow with create-pr and create-diagram skills](https://www.linkedin.com/feed/update/urn:li:activity:7426573992695791616?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7426573992695791616%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29)
📅 2026-02-26 · 🌐 Reader Share Sheet iOS

**Summary:** AI agents can build software much faster by handling repetitive coding tasks. Engineers focus more on designing clear rules and feedback loops to guide these agents. This approach improves reliability and speeds up development without manual coding.

---

## [Peter K.’s Post](https://www.linkedin.com/feed/update/urn:li:activity:7427785041746837504?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7427785041746837504%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29)
📅 2026-02-26 · 🌐 Reader Share Sheet iOS

**Summary:** Building OneLake in Microsoft Fabric requires careful planning from the start. Good governance and metadata keep data organized and secure. Virtualization helps combine data without losing control or performance.

---

## [Dennes Torres’ Post](https://www.linkedin.com/feed/update/urn:li:activity:7428897490407505920?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7428897490407505920%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29)
📅 2026-02-26 · 🌐 Reader Share Sheet iOS

**Summary:** Dennes Torres explains how Variable Libraries in Microsoft Fabric help automate Lakehouse deployments without manual shortcut fixes. This makes deployment cleaner, safer, and more confident. The video guides users on managing data across development stages effectively.

---

## [Gregor Brunner’s Post](https://www.linkedin.com/feed/update/urn:li:activity:7427658248096501760?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7427658248096501760%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29)
📅 2026-02-26 · 🌐 Reader Share Sheet iOS

**Summary:** Gregor Brunner shared a blog post by his colleague Klaus about improving Power BI models. They found 16 easy ways to make models smaller using #MeasureKiller. The post helps avoid problems like model bloat from calculated columns.

---

## [Adrian Chodkowski’s Post](https://www.linkedin.com/feed/update/urn:li:activity:7429437904923328512?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7429437904923328512%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29)
📅 2026-02-26 · 🌐 Reader Share Sheet iOS

**Summary:** Delta Lake is a storage layer built on top of Parquet that adds reliability, ACID transactions, and data change tracking. Parquet is best for fast, read-only analytics with static data. Delta Lake is better for data that changes often and needs updates, deletes, and time travel.

---

## [Tom Baeyens’ Post](https://www.linkedin.com/feed/update/urn:li:activity:7429847820611858432?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7429847820611858432%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29)
📅 2026-02-26 · 🌐 Reader Share Sheet iOS

**Summary:** A data product is a trusted, well-defined dataset owned by a team and made easy for users to find and understand. It focuses on data quality, clear ownership, and how data is consumed, not just how it moves. Good data strategies include governance, performance, and aligning data with business goals for better decisions.

---

## [Keeping Spark, OneLake, and Mirroring Reliable in Microsoft Fabric](https://christopherfinlan.com/2026/02/25/fabric-spark-failure-playbook-onelake-mirroring-production/)
📅 2026-02-25 · 🌐 Reader Share Sheet iOS

**Summary:** Microsoft Fabric can have hidden delays and errors when Spark, OneLake, and mirroring work together under heavy use. Monitoring job success alone is not enough; teams need to check data freshness, permissions, and capacity to catch problems early. Using automated checks and clear triage steps helps keep data reliable and avoids surprises.

---

## [Tom Baeyens’ Post](https://www.linkedin.com/posts/tombaeyens_i-am-a-data-architect-what-use-are-data-activity-7432388752007729152-suAM?utm_source=share&utm_medium=member_ios&rcm=ACoAAA4TApsBpcD7dMto9tdEqMhSTfRhiYAy83E)
📅 2026-02-25 · 🌐 Reader Share Sheet iOS

**Summary:** Data contracts help data architects maintain quality across different domains without centralizing work. They provide a standard way to track and manage data quality with automation and version control. This improves visibility, supports reporting, and reduces manual audits.

---

## [Barney Lawrence’s Post](https://www.linkedin.com/posts/barneylawrence_pros-and-cons-of-approval-workflows-in-purview-activity-7432083045802971137-QR4Q?utm_source=share&utm_medium=member_ios&rcm=ACoAAA4TApsBpcD7dMto9tdEqMhSTfRhiYAy83E)
📅 2026-02-25 · 🌐 Reader Share Sheet iOS

**Summary:** Barney Lawrence shared an update about the new approval workflows feature in Purview Data Governance. He invites users to try it and give feedback. The feature is still limited but could improve with future updates.

---

## [Tom Baeyens’ Post](https://www.linkedin.com/posts/tombaeyens_i-hope-you-are-not-calling-your-data-pipelines-activity-7429847820611858432-eMow?utm_source=share&utm_medium=member_ios&rcm=ACoAAA4TApsBpcD7dMto9tdEqMhSTfRhiYAy83E)
📅 2026-02-23 · 🌐 Reader Share Sheet iOS

**Summary:** A data product is a carefully prepared dataset made for a clear purpose. It has clear ownership, metadata, and guarantees for users. Data pipelines help create data products but are just one part of them.

---

## [Iurii (Yurri) Iurchenko, FACHDM’s Post](https://www.linkedin.com/posts/4iurchenko_drawio-library-for-microsoft-fabric-activity-7431404923138785280-XjMC?utm_source=share&utm_medium=member_ios&rcm=ACoAAA4TApsBpcD7dMto9tdEqMhSTfRhiYAy83E)
📅 2026-02-23 · 🌐 Reader Share Sheet iOS

**Summary:** Iurii Iurchenko wrote a blog about a new Draw.IO library for Microsoft Fabric. He encourages people to like and share his post to help others. The tool helps teams work better using diagrams.

---

## [Boris Cherny’s vision for Claude Code isn’t about flashy demos or conversational tricks. It’s about making AI feel like real infrastructure inside the development workflow.](https://www.instagram.com/p/DUVNEohCfX1/?img_index=2&igsh=MWt2ZWtkbGtveTh3Nw==)
📅 2026-02-17 · 🌐 Reader Share Sheet iOS

**Summary:** Boris Cherny wants Claude Code to be a natural part of developers' workflow, not a flashy tool. It helps developers save time on repetitive tasks and focus on important decisions. Claude Code supports long projects and works smoothly with existing tools.

---

## [Adrian Chodkowski’s Post](https://www.linkedin.com/posts/adriansql_dataengineering-deltalake-databricks-activity-7429437904923328512-ivCN?utm_source=share&utm_medium=member_ios&rcm=ACoAAA4TApsBpcD7dMto9tdEqMhSTfRhiYAy83E)
📅 2026-02-17 · 🌐 Reader Share Sheet iOS

**Summary:** Delta Lake 3.2+ now has Row Tracking to follow every change in a table. Each row gets a unique ID that stays the same even after updates. You just need to enable it with a simple table property to start using this helpful feature.

---

## [Aleksi Partanen’s Post](https://www.linkedin.com/posts/aleksi-partanen_microsoftfabric-azuredevops-dataengineering-activity-7429426813787070464-0Jvc?utm_source=share&utm_medium=member_ios&rcm=ACoAAA4TApsBpcD7dMto9tdEqMhSTfRhiYAy83E)
📅 2026-02-17 · 🌐 Reader Share Sheet iOS

**Summary:** Microsoft Fabric items are owned by personal accounts, causing pipeline failures when passwords change. Using a Service Principal to run deployment pipelines solves this problem. This makes production environments more reliable and stable.

---

## [Alex Powers’ Post](https://www.linkedin.com/feed/update/urn:li:activity:7420501150975713280?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7420501150975713280%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29)
📅 2026-02-17 · 🌐 Reader Share Sheet iOS

**Summary:** Alex Powers wants to improve AI development by giving clear instructions. He learned from Jeff Blankenburg that copying code without understanding it slows progress. Alex is working on a project that challenges him to find better solutions and strong business goals.

---

## [Tobias Müller’s Post](https://www.linkedin.com/feed/update/urn:li:activity:7429117368427241472?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7429117368427241472%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29)
📅 2026-02-17 · 🌐 Reader Share Sheet iOS

**Summary:** Tobias Müller created polyglot, a fast Rust SQL transpiler supporting over 30 SQL dialects with full test coverage. He built it using AI tools like Claude and GPT-5.3-Codex within three weeks, showing strong AI-assisted development potential. The project relies on sqlglot’s open-source code and includes a Wasm/TypeScript SDK for browsers and servers.

---

## [Mohammed Adnan’s Post](https://www.linkedin.com/posts/mohammedadnant_powerbi-microsoftfabric-opensource-activity-7429223077005369344-6WTp?utm_source=share&utm_medium=member_ios&rcm=ACoAAA4TApsBpcD7dMto9tdEqMhSTfRhiYAy83E)
📅 2026-02-17 · 🌐 Reader Share Sheet iOS

**Summary:** PBIP Studio is a free, open-source Windows toolkit that simplifies Power BI and Fabric development by automating repetitive tasks. It helps with data migration, model renaming, and local metadata management while running everything locally for privacy. The project invites the community to contribute and improve the tool together.

---

## [Quickly add great reads from the Readwise community to your library](https://blog.readwise.io/p/96321ba4-4a2c-49b9-babd-630cb69255c7/)
📅 2026-02-16 · 🌐 readwise onboarding

**Summary:** You can easily save documents to read later using Reader's browser extension or by uploading your files. To find popular content, just click a button to browse highlighted articles, PDFs, and tweets from other users. You can also access your saved documents from the Add Documents button in the app.

---

## [Reader: Frequently Asked Questions](https://blog.readwise.io/p/f8c0f71c-fe5f-4025-af57-f9f65c53fed7/)
📅 2026-02-16 · 🌐 readwise onboarding

**Summary:** Reader lets you save and highlight articles on web and mobile, syncing all notes with Readwise and your apps. You can use keyboard shortcuts on web and a browser extension to save and highlight content easily. Reader organizes your saved articles and helps you read without distractions, while keeping all highlights synced across devices.

---

## [Getting Started with Reader](https://blog.readwise.io/p/bf87944f-b0fe-4f08-a461-f75ab8aded6a/)
📅 2026-02-16 · 🌐 readwise onboarding

**Summary:** Reader is a powerful reading app that lets you save, highlight, and annotate many types of documents using keyboard shortcuts or mobile gestures. It also offers features like text-to-speech, a web highlighter, and YouTube video notes to boost your productivity. The app is constantly improving based on user feedback and includes helpful guides and support.

---
