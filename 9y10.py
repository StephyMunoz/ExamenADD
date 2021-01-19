import pandas as pd
from pymongo import MongoClient
import csv

client = pymongo.MongoClient("mongodb+srv://esfot:esfot@cluster0.845nq.mongodb.net/animalsandRecycling?retryWrites=true&w=majority")
try:
    client.admin.command('ismaster')
    print('MongoDB Atlas connection: Success')
except ConnectionFailure as e:
    print('MongoDB Atlas connection: failed', e)


db = client.get_database('elecciones_2021')
collection = db.get_collection('eleccionesgenerales2021')


dfMA = pd.DataFrame(list(collection.find()))

dfMA

dfMA.to_csv('elecciones2021.csv', index=True)