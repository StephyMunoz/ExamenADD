from facebook_scraper import get_posts
import json
import time
from pymongo import MongoClient


db = MongoClient('mongodb://localhost:27017').elecciones2021

i=1
for post in get_posts('elecciones2021', pages=1000):
    print(i)
    i=i+1
    time.sleep(5)
    
    id=post['post_id']
    doc={}
     
    doc['id']=id
    
    mydate=post['time']
    
    try:
        doc['texto']=post['text']
        doc['date']=mydate.timestamp()
        doc['likes']=post['likes']
        doc['comments']=post['comments']
        doc['shares']=post['shares']

        doc['post_url']=post['post_url']
        db.eleccionesgenerales.insert(doc)

    
        print("guardado exitosamente")

    except Exception as e:    
        print("no se pudo grabar:" + str(e))