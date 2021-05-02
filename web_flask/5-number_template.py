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


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythonF(text):
    """ comment """
    text = text.replace('_', ' ')
    return ('Python {}'.format(text))


@app.route('/number/<int:n>')
def number(n):
    """ comment """
    return '%s is a number' % n


@app.route('/number_template/<int:n>')
def number_template(n):
    """ comment """
    return (render_template('5-number.html', n=n))


if __name__ == '__main__':
    """ comment """
    app.run(host='0.0.0.0', debug=False)
