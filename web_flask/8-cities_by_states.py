#!/usr/bin/python3
""" Start Flask"""
from models import strorage
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities():
    """ Display a HTML page """
    states = storage.all("State")
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown(exc):
    """ Remove the curreny sqlalchemy session """
    storage.close()
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
