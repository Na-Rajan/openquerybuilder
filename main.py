from .config import Config
from .db_connector import DBConnector
from .schema_explorer import SchemaExplorer
from .query_generator import QueryGenerator

class QueryBuilder:
    def __init__(self, db_configs, openai_api_key):
        self.config = Config(db_configs, openai_api_key)
        self.connectors = [DBConnector(cfg) for cfg in self.config.db_configs]
        self.schema_metadata = []

    def load_schema(self):
        for connector in self.connectors:
            explorer = SchemaExplorer(connector)
            self.schema_metadata.extend(explorer.fetch_schema())

    def generate_query(self, prompt):
        generator = QueryGenerator(self.config.openai_api_key, self.schema_metadata)
        return generator.generate_query(prompt)