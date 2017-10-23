import datetime
from bottle import request, response
from server.app import app, conn, BASE_API
from server.models.bots import BotRepository


API = BASE_API + '/bots'


@app.get(API)
def _get_all():
    repo = BotRepository(conn)
    return {'bots': repo.get_all(request.query)}


@app.get(API + '/<id:int>')
def _get_by_id(id):
    repo = BotRepository(conn)
    return repo.get_by_id(id)


@app.post(API)
def _post():
    repo = BotRepository(conn)

    if request.json is None:
        response.status = 400
        return

    result = repo.insert(request.json)
    response.status = 201
    return result


@app.put(API)
def _put():
    repo = BotRepository(conn)

    if request.json is None:
        response.status = 400
        return

    repo.update(request.json)
    return {'updated_at': datetime.datetime.utcnow()}