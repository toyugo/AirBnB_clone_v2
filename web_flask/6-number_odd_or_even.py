from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    return 'HBNB'


@app.route('/c/<text>')
def c(text):
    return 'C {}'.format(text)


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    text = text.replace('_', ' ')
    return ('Python {}'.format(text))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return '%s is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return (render_template('5-number.html', n=n))


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    if n % 2 == 1:
        pV = 'odd'
    else:
        pV = 'even'
    return render_template('6-number_odd_or_even.html', n=n, pairValue=pV)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
