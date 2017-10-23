# TwitMasto

## Installation

### Server-side

* Install [python 3](https://www.python.org/)
* Create your virtual environment (e.g. `python -m venv .env/`)
* Activate your venv
    * Windows: `<venv-directory>\Scripts\activate.bat`
    * Unix: `source <venv-directory>/bin/activate`
* Install dependencies: `pip install -r requirements.txt`

### Client-side

* Install [node](https://nodejs.org/)
* (Optional: install [yarn](https://yarnpkg.com/))
* Install dependencies
    * `npm install` OR `yarn install`

## Run

* Run the server: `npm start`
    * _If on Unix, change package.json>scripts>start to `<venv-directory>/bin/python3 run.py`_

## Building the client side

* `npm run build`
* You can also watch for changes and rebuild with `npm run watch`