import tweepy
from server.app import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, \
    ACCESS_SECRET, app, BASE_API

API = BASE_API + '/twitter-api'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


@app.get(API + '/lists')
def _get_lists():
    result = api.lists_all()
    return {'lists': result}
