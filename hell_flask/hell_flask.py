#!/usr/bin/env python

import flask
import getBusStopData

# Create the application.
APP = flask.Flask(__name__)


@APP.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('home.html',buses=getBusStopData.getTime())


if __name__ == '__main__':
    APP.debug=True
    APP.run()
