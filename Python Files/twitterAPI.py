from twitter import *

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

def TwitterAPI(hotword):
    twitter = Twitter(auth=OAuth(access_token, access_token_secret, consumer_key, consumer_secret))

    results = twitter.users.search(q = hotword)
    accounts=[]
    id=[]

    for user in results:
        if(not user["protected"]):
            accounts.append(user["screen_name"])
            id.append(user["id"])
    return accounts,id
    