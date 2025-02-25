#!/usr/bin/python3
""" Start Flask"""
from models import strorage
from models import *
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hbnb_filters', strict_slashes=False)
def cities():
    """ Display a HTML page """
    states = storage.all("State").values()
    amenities = strorage.all("Amenity").values()
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(exc):
    """ Remove the curreny sqlalchemy session """
    storage.close()
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')