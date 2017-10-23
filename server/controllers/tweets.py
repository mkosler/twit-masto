from bottle import request, response
from server.app import app, conn, BASE_API
from server.models.tweets import TweetRepository


API = BASE_API + '/tweets'


@app.get(API)
def _get_all():
    repo = TweetRepository(conn)
    return {'tweets': repo.get_all(request.query)}


@app.get(API + '/<id:int>')
def _get_by_id(id):
    repo = TweetRepository(conn)
    return repo.get_by_id(id)


@app.post(API)
def _post():
    repo = TweetRepository(conn)

    if request.json is None:
        response.status = 400
        return

    result = repo.insert(request.json)
    response.status = 201
    return result
