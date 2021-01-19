from argparse import ArgumentParser
import requests
import pymongo 
from pymongo.errors import ConnectionFailure
from bson import json_util
from bson import ObjectId
import couchdb
import dns
import json
from bson.json_util import loads

CLIENT = pymongo.MongoClient('mongodb://localhost:27017')

try:
    CLIENT.admin.command('ismaster')
    print('MongoDB connection: Success')
except ConnectionFailure as e:
    print('MongoDB connection: failed', e)
    
client = pymongo.MongoClient("mongodb+srv://esfot:esfot@cluster0.845nq.mongodb.net/twitter_animals?retryWrites=true&w=majority")
DBm = client.get_database('twitter_animals')
DBma = DBm.animalsAndRecycling

try:
    client.admin.command('ismaster')
    print('MongoDB Atlas connection: Success')
except ConnectionFailure as e:
    print('MongoDB Atlas connection: failed', e)
    

DBS = ['twitter_animals']

for db in DBS:
    if db not in ('admin', 'local','config'):  
        cols = CLIENT[db].list_collection_names()  
        for col in cols:
            print('Querying documents from collection {} in database {}'.format(col, db))
            for x in CLIENT[db][col].find():  
                try:
                    documents = json.loads(json_util.dumps(x))
                    documents["_id"]=str(documents["_id"]["$oid"])
                    print(documents)
                    DBma.insert_one(documents)
                    print("saved in mongo atlas")

                except TypeError as t:

                    print('current document raised error: {}'.format(t))
                    SKIPPED.append(x)  # creating list of skipped documents for later analysis
                    continue    # continue to next document
                except Exception as e:
                    raise e