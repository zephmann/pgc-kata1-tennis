# :coding: utf-8

import os

from flask import Flask, request

import tennis

app = Flask(__name__, static_folder="../../build", static_url_path="/")


@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.errorhandler(404)
def not_found(e):
    return app.send_static_file("index.html")


@app.route("/api/score")
def get_formatted_score():
    server = int(request.args.get("server", 0))
    opponent = int(request.args.get("opponent", 0))

    return {'score': tennis.score((server, opponent))}


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=os.getenv("PORT", 80))
