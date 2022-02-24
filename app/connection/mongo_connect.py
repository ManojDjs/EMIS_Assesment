from pymongo import MongoClient
class DB_instance:
    def __init__(self):
        self.connection_string="mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false"

    def connect(self):
        self.client = MongoClient(self.connection_string)
        self.db = self.client.Client_H
    
    def closeConnection(self):
        self.client.close()
    
    def Find_patient_id(self):
        pass

    def insert(self,Table_name,Data):
        self.connect()
        collection = self.db[Table_name]
        insertion_data=collection.insert_many(Data)
        self.closeConnection() 
        return insertion_data
        
        