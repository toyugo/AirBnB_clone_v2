#!/usr/bin/python3
"""
    commentaire
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters_route():
    """ commentaire """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template(
            '10-hbnb_filters.html',
            states=states,
            amenities=amenities)


@app.teardown_appcontext
def teardown_db(exception):
    """ commentaire """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
