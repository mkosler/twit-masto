import os
import json
import datetime
import psycopg2
import psycopg2.extras
from bottle import Bottle, JSONPlugin, static_file, request, load


BASE_API = '/api/v1'


def _datetime_handler(x):
    if isinstance(x, datetime.datetime):
        return x.isoformat()
    raise TypeError('unknown type')


app = Bottle()
app.uninstall(True)
app.install(JSONPlugin(
    json_dumps=lambda body: json.dumps(body, default=_datetime_handler)
))
_public_root = os.path.join(os.getcwd(), 'public/')
_conn_string = os.environ['TWITMASTO_CONNECTION_STRING']
conn = psycopg2.connect(
    _conn_string,
    cursor_factory=psycopg2.extras.RealDictCursor
)


# Hooks
@app.hook('before_request')
def _strip_path():
    request.environ['PATH_INFO'] = request.environ['PATH_INFO'].rstrip('/')


# Register controllers
load('server.controllers.bots')


# Static routes
@app.route('/public/<filepath:path>')
def serve_public(filepath):
    return static_file(filepath, _public_root)


@app.route('/')
@app.route('/<path:path>')
def index(path=None):
    return static_file('index.html', _public_root)
