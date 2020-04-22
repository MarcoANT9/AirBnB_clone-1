#!/usr/bin/python3
""" This script starts a Flask web application. """
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close_db(self):
    """ Closes the database. """
    storage.close()

@app.route('/states_list', strict_slashes=False)
def state_listing():
    """ List all states. """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
