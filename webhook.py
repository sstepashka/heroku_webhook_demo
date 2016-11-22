# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from flask import make_response
from flask import jsonify

import logging

app = Flask(__name__)
log = logging.getLogger('gunicorn.glogging.Logger')

stream_handler = logging.StreamHandler()

log.addHandler(stream_handler)

app.logger.addHandler(stream_handler)
app.logger.setLevel(logging.INFO)


app.config['DEBUG'] = True
app.debug = True


@app.route('/')
@app.route('/index')
def index():
    return "This is the application mynote & I'm alive"


@app.route('/webhook', methods=['POST'])
def webhook():
    params = request.get_json(silent=True, force=True)

    log.info("Params: %s", repr(params))

    speech = "speech text example 1"
    displayText = "display text example"
    data = {
        "example_key": "example_value"
    }

    contextOut = [
        {
            "name": "context_name_example",
            "lifespan": 5,
            "parameters": {
                "param_1": "param_1_value"
            }
        }
    ]

    source = "webhook_source"

    return make_response(
        jsonify(
            {
                "speech": speech,
                "displayText": displayText,
                "data": data,
                "contextOut": contextOut,
                "source": source
            }
        )
    )
