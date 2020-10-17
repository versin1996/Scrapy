from pymongo import MongoClient


class DB:
    def __init__(self, database, collection):
        client = MongoClient()
        self.collection = client[database][collection]
    
    def insert(self, doc):
        self.collection.insert(doc)

