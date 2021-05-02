#!/usr/bin/python3
"""
    setup 3
"""
from flask import Flask
app = Flask(__name__)



@app.route('/', strict_slashes=False)
def index():
    """ comment """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ comment """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ comment """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)

if __name__ == '__main__':
    """ comment """
    app.run(host='0.0.0.0', debug=False)
