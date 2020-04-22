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


@app.route('/states-list', strict_slashes=False)
def state_listing():
    """ List all states. """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def city_in_state_list():
    """ List all cities in all states. """
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


@app.route('/states', strict_slashes=False)
def print_all_states():
    """ List all states.
        stat = 0 → List all states, do nothing more.
    """
    states = storage.all(State).values()
    return render_template('9-states.html', states=states, stat=0)


@app.route('/states/<id>', strict_slashes=False)
def state_by_demand(id):
    """ List all the cities in a state given by the user.
        stat = 1 → List all cities in a state or not found according to its
                   name.
    """
    states = storage.all(State).values()
    for state in states:
        if state.id == id:
            return render_template('9-states.html', state_name=state.name,
                                   cities=state.cities, stat=1)

    return render_template('9-states.html', state_name='None',
                           cities=state.cities, stat=1)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
