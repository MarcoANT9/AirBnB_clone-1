#!/usr/bin/python3
""" This script starts a Flask web application. """
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """ Default return """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Return for this path """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_print(text):
    """ Prints the word 'C' and whatever is in the path. """
    text = text.replace("_", " ")
    return "C %s" % text


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def p_print(text='is cool'):
    """ Prints the word 'Python ' and whatever is in the path. """
    text = text.replace("_", " ")
    return "Python %s" % text


@app.route('/number/<int:n>', strict_slashes=False)
def number_print(n):
    """ Prints 'n is a number' if n is an integer. """
    return "%d is a number" % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def html_import(n):
    """Displays an HTML page only if n is an integer. """
    return render_template('5-number.html', name=n)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
