# create virtual env (windows cmd) - py -m venv env
# start virtual env (windows cmd) - env\Scripts\activate
# set app environment (windows cmd) - set FLASK_APP=app.py
# set app debug (windows cmd) - set FLASK_DEBUG=1

from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>hello world</h1>' # returns string to webpage
    
    