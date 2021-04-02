# :coding: utf-8

from flask import Flask, request

import tennis

app = Flask(__name__)


@app.route('/score')
def get_formatted_score():
    server = int(request.args.get("server", 0))
    opponent = int(request.args.get("opponent", 0))

    return {'score': tennis.score((server, opponent))}