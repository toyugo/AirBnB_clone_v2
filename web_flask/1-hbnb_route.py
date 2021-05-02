#!/usr/bin/python3
"""
    setup 2 routes
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """simple route"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """simple route"""
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
