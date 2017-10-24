import os
import json
import datetime
import psycopg2
import psycopg2.extras
from bottle import Bottle, JSONPlugin, static_file, request, load


BASE_API = '/api/v1'
CONSUMER_KEY = os.environ['TWITTER_CONSUMER_KEY']
CONSUMER_SECRET = os.environ['TWITTER_CONSUMER_SECRET']
ACCESS_TOKEN = os.environ['TWITTER_ACCESS_TOKEN']
ACCESS_SECRET = os.environ['TWITTER_ACCESS_SECRET']
_conn_string = os.environ['TWITMASTO_CONNECTION_STRING']


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
load('server.controllers.twitter_api')


# Static routes
@app.route('/public/<filepath:path>')
def serve_public(filepath):
    return static_file(filepath, _public_root)


@app.route('/')
@app.route('/<path:path>')
def index(path=None):
    return static_file('index.html', _public_root)
