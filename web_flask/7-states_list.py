#!/usr/bin/python3
""" Start Flask"""
from models import strorage
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states():
    """ Display a HTML page """
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exc):
    """ Remove the curreny sqlalchemy session """
    storage.close()
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')