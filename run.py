from server import app
from bottle import run, debug


if __name__ == '__main__':
    debug(True)
    run(app, port=1323)
