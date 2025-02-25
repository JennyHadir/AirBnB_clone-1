#!/usr/bin/python3
""" Start Flask web app """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ Return Hello hbnb """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello():
    """ Return HBNB"""
    return 'HBNB'
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
