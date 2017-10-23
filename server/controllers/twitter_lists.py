from bottle import request
from server.app import app, conn, BASE_API
from server.models.twitter_lists import TwitterListRepository


API = BASE_API + '/twitter-list'


@app.get(API)
def _get_all():
    repo = TwitterListRepository(conn)
    return {'twitter_lists': repo.get_all(request.query)}


@app.get(API + '/<id:int>')
def _get_by_id(id):
    repo = TwitterListRepository(conn)
    return repo.get_by_id(id)


@app.post(API)
def _post():
    repo = TwitterListRepository(conn)
    if request.json is None:
        raise ValueError
    return repo.insert(request.json)
