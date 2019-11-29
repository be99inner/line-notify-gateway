#!/bin/env python3
"""
Line Notify Gateway Application
License: MIT
"""

import logging
from flask import Flask, render_template

import manage_logs

LOG_PATH = 'logs/line-notify-gateway.log'

app = Flask(__name__)


@app.route('/')
def index():
    """
    Show summary information on web browser.
    """
    logging.basicConfig(filename=LOG_PATH, level=logging.INFO)
    return render_template('index.html', name='index')


@app.route('/webhook')
def webhook():
    """
    Firing message to Line notify API when it's triggered.
    """


@app.route('/logs')
def logs():
    """
    Display logs on web browser.
    """
    file = open(LOG_PATH, 'r+')
    content = file.read()
    logging.basicConfig(filename=LOG_PATH, level=logging.INFO)
    return render_template('logs.html', text=content, name='logs')


@app.route('/metrics')
def metrics():
    """
    Expose metrics for monitoring tools.
    """


if __name__ == "__main__":
    manage_logs.init_log(LOG_PATH)
    app.run()
