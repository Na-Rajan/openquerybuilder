import sqlalchemy
from sqlalchemy import create_engine

class DBConnector:
    def __init__(self, db_config):
        self.db_type = db_config["type"]
        self.connection_string = db_config["connection_string"]
        self.engine = create_engine(self.connection_string)

    def get_connection(self):
        return self.engine.connect()
