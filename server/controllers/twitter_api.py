import tweepy
from bottle import request, response
from server.app import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, \
    ACCESS_SECRET, app, BASE_API

API = BASE_API + '/twitter-api'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
tweepy.debug(True, 10)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


@app.get(API + '/lists')
def _get_lists():
    return {'lists': api.lists_all()}


@app.get(API + '/lists/statuses')
def _get_statuses_for_list():
    owner_id = request.query.get('owner_id')
    slug = request.query.get('slug')
    count = request.query.get('count', 5)
    return {
        'statuses': api.list_timeline(
            owner_id=owner_id,
            slug=slug,
            count=count
        )
    }
