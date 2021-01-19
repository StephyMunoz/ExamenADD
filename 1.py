import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

ckey = "xhj1i3hWIcekidPhdmri9a9Eo"
csecret = "jHANPKyrFV0HEEfKSVwtYfABn2elj5E66oTEGeooisvbB5a5RU"
atoken = "182982111-xJW5g5pzl6QmbBGLprMo34lOkgj32FFWn2JMCDG3"
asecret = "6g5LYSm3agQXl02RHHXW85DRQenOWL2NUFREfMiQzKdXH"

class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print ("SAVED" + str(doc) +"=>" + str(data))
        except:
            print ("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''========couchdb'=========='''
server = couchdb.Server('http://admin:2910@localhost:5984/')  #('http://115.146.93.184:5984/')
try:
    db = server.create('elecciones_2021')
except:
    db = server['elecciones 2021']
    
'''===============FILTERS=============='''    

twitterStream.filter(track=['Ecuador', 'elecciones generales 2021'])