#!/usr/bin/python3
"""HNG Backend Stage 0"""

from flask import Flask

app = Flask(__name__)


@app.route("/", methods=['GET'])
def display_info():
    return "Hi"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
