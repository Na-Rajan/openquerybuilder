# 🧠 OpenQueryBuilder

**AI-powered SQL query builder for any database.**  
Connect to Oracle, Snowflake, PostgreSQL, and more. Use natural language to generate SQL or PL/SQL queries with OpenAI.

---

## 🚀 Features

- 🔗 Connect to multiple databases
- 🧠 Understand schema automatically
- 💬 Generate queries from natural language
- 🛡 Safe and customizable
- 🧪 Easy to test and extend

🛠 Supported Databases
Oracle

Snowflake

PostgreSQL

MySQL

SQL Server

SQLite

🔐 Security
OpenAI key is user-provided

Input sanitization included

Optional read-only mode

🤝 Contributing
Pull requests welcome! Please include tests and examples.
---

## 📦 Installation


```bash
pip install -r requirements.txt
----------------------------------------------------------------------------------------------

from openquerybuilder.main import QueryBuilder

qb = QueryBuilder(
    db_configs=[
        {"type": "oracle", "connection_string": "oracle+cx_oracle://user:pass@host:port/db"},
        {"type": "snowflake", "connection_string": "snowflake://user:pass@account/db/schema"}
    ],
    openai_api_key="your-openai-key"
)

qb.load_schema()
query = qb.generate_query("Show top 5 products by revenue")
print(query)
--------------------------------------------------------------------

