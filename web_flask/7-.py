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

@app.route('/python', defaults= {'text': 'is magic'})
@app.route('/python/', defaults= {'text': 'is magic'})
@app.route('/python/<text>')
def python(text):
	text = text.replace('_', ' ')
	return ('Python {}'.format(text))

@app.route('/number/<int:n>')
def number(n):
	return '%s is a number' % n

@app.route('/number_template/<int:n>')
def number_template(n):
	return (render_template('5-number.html', n=n))

@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
	if n % 2 == 1:
		pairValue = 'odd'
	else:
		pairValue = 'even'	
	return render_template('6-number_odd_or_even.html', n=n, pairValue=pairValue)

#@app.teardown_appcontext
#def 

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=False)
