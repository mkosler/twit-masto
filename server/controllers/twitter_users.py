from bottle import request
from server.app import app, conn, BASE_API
from server.models.twitter_users import TwitterUserRepository


API = BASE_API + '/twitter-users'


@app.get(API)
def _get_all():
    repo = TwitterUserRepository(conn)
    return {'twitter_users': repo.get_all(request.query)}


@app.get(API + '/<id:int>')
def _get_by_id(id):
    repo = TwitterUserRepository(conn)
    return repo.get_by_id(id)


@app.post(API)
def _post():
    repo = TwitterUserRepository(conn)
    if request.json is None:
        raise ValueError
    return repo.insert(request.json)
