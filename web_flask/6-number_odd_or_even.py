#!/usr/bin/python3
"""
    setup 3
"""
from flask import Flask
from flask import render_template
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


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ comment """
    return '{:d} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ comment """
    return (render_template('5-number.html', n=n))


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """ comment """
    if n % 2 == 1:
        pV = 'odd'
    else:
        pV = 'even'
    return render_template('6-number_odd_or_even.html', n=n, pairValue=pV)


if __name__ == '__main__':
    """ comment """
    app.run(host='0.0.0.0', debug=False)
