#!/usr/bin/python3
""" Start Flask"""
from models import strorage
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def cities():
    """ Display a HTML page """
    states = storage.all("State")
    return render_template('9-states.py', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id():
    """ Display a HTML page """
    for state in storage.all("State").values():
        if state.id == id:
            return render_template('9-states.py', states=states)
    return render_template('9-states.py')


@app.teardown_appcontext
def teardown(exc):
    """ Remove the curreny sqlalchemy session """
    storage.close()
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
