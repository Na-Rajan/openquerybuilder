class SchemaExplorer:
    def __init__(self, connector):
        self.connector = connector

    def fetch_schema(self):
        query = """
        SELECT table_name, column_name, data_type
        FROM information_schema.columns
        WHERE table_schema NOT IN ('information_schema', 'pg_catalog')
        """
        with self.connector.get_connection() as conn:
            result = conn.execute(query)
            return [dict(row) for row in result]