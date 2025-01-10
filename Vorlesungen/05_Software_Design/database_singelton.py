import os
from tinydb import TinyDB

class DatabaseConnector:
    
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.json')

        return cls.__instance

    def get_table(self, table_name: str):
        #return TinyDB(self.path, storage=serializer).table(table_name)
        return TinyDB(self.path).table(table_name)

if __name__ == '__main__':

    db_connection_1 = DatabaseConnector().get_table("devices")
    db_connection_2 = DatabaseConnector().get_table("devices")

    result1 = db_connection_1.all()
    result2 = db_connection_2.all()
    print(result1)
