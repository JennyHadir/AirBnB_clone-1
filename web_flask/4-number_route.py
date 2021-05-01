#!/usr/bin/python3
""" Start Flask web app"""
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


@app.route('/c/<text>', strict_slashes=False)
def C(text):
    """ Return C followed by the value of text"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """ Return python followed by text"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def numb(n):
    """ Return n if it's a number"""
    if isinstance(n, int):
        return '{} is a number'.format(n)
if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port='5000')
