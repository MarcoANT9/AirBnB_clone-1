#!/usr/bin/python3
""" This script starts a Flask web application. """
from flask import Flask

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
    return "C %s" % text


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
