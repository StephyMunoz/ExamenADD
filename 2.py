import pandas as pd
from bs4 import BeautifulSoup
import requests
import time
from pymongo import MongoClient
import json

db = MongoClient('mongodb://localhost:27017').usedcars

Model=[]
Year=[]
Negociable=[]
Price=[]

def find_2nd(string, substring):
    return string.find(substring, substring.find(substring)+1)

def find_1st(string, substring):
    return string.find(substring, substring.find(substring))

response = requests.get('https://ecuador.patiotuerca.com/usados/pichincha-quito/autos?type_autos_moderated=moderated')
soup = BeautifulSoup(response.content,"lxml")

post_model=soup.find_all("h4", class_="bold size-h6 left")
for element in post_model:
    element=str(element)
    limpio=str(element[find_1st(element,'>')+1:find_2nd(element,'<')])
    Model.append(limpio.strip())
    #print(limpio.strip())

post_year=soup.find_all("span", class_="year")
for element in post_year:
    element=str(element)
    limpio=str(element[find_1st(element,'>')+1:find_2nd(element,'<')])
    Year.append(str(limpio.strip()))


post_negociable=soup.find_all("span", class_="latam-secondary-text text-lighten-2 negotiable-txt left")
for element in post_year:
    element=str(element)
    limpio=str(element[find_1st(element,'>')+1:find_2nd(element,'<')])
    Negociable.append(str(limpio.strip()))



post_price=soup.find_all("span", class_="left share-value")
for element in post_price:
    element=str(element)
    limpio=str(element[find_1st(element,'>')+1:find_2nd(element,'<')])
    Price.append(str(limpio.strip()))


i=0
for j in post_model:
    doc={}
    id=i
    try:
        doc = {'model':Model[i],'year': Year[i],'negociable': Negociable[i],'price':Price[i]}
        db.autos.insert_one(doc)
        print("guardado exitosamente")
    except Exception as e:    
        print("no se pudo grabar:" + str(e))