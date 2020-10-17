import pymongo
from tqdm import tqdm
from pymongo import MongoClient
from itertools import chain

class DB:
    def __init__(self, database, collection):
        client = MongoClient()
        self.collection = client[database][collection]
    
    def insert(self, doc):
        self.collection.insert_one(doc)

    def find(self, query, filter=None):
        if not filter:
            return self.collection.find(query)
        return self.collection.find(query, filter)
    
    def find_and_sort(self, query, sort_field, filter=None):
        if not filter:
            ret = list(self.collection.find(query, filter).sort(sort_field, pymongo.ASCENDING))
            pages = [(i['page'], i['id']) for i in ret]
            if pages[-1][0] - pages[0][0] + 1 != len(pages):
                return None
            return ret
        return self.collection.find(query).sort(sort_field, pymongo.ASCENDING)

    def find_one(self, query, filter=None):
        if not filter:
            return self.collection.find_one(query)
        return self.collection.find_one(query, filter)
    
    def count(self, query={}):
        return self.collection.find(query).count()

def merge(category):
    result_db = DB('bianju', category)
    if result_db.count() != 0:
        return
    basic_info_db = DB('bianju', 'basicInfo_{}'.format(category))
    brief_db = DB('bianju', 'brief_{}'.format(category))
    content_db = DB('bianju', 'content_{}'.format(category))
    basic_info = list(basic_info_db.find({}, {'_id': 0}))  
    for info in tqdm(basic_info):
        try:
            brief = brief_db.find_one({'id': info['id']}, {'_id': 0})
            info.update(brief)
            contents = content_db.find_and_sort({'id': info['id']}, 'page')
            if contents:
                contents = [content['content'] for content in contents]
                contents = list(chain(*contents))
                info['content'] = contents
                result_db.insert(info)
        except:
            continue

if __name__ == '__main__':
    categorys = ['screenplay', 'netscreenplay', 'telescript', 'nettelescript', 'microfilm', 'novel', 'other', 'famous', 'recommend', 'free']
    for category in categorys:
        merge(category)
