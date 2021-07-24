import tweepy as tw
import time
from datetime import datetime
import json

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

def message(i):
    recipient_id = i
    # text to be sent
    text = "test"+str(datetime.now().strftime("%H:%M:%S"))
    direct_message = api.send_direct_message(recipient_id, text)

def ats(accNames):
    print(type(accNames))
    accNames=list(map(str,accNames.split(',')))
    print(accNames)

    testGroup=[]
    
    for i in accNames:
        user = api.get_user(i)  
        ID = user.id_str
        testGroup.append(int(ID))
    
    print(testGroup)

    testGroup=[1282953845342003200]
    
    for i in testGroup:
        message(i)
        time.sleep(5)
