#!/usr/bin/python3
"""HNG Backend Stage 0"""

from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)


@app.route("/", methods=['GET'])
def display_info():
    info = {
            "email": "toruwalt1997@gmail.com",
            "current_datetime": datetime.now().isoformat(),
            "github_url": "https://github.com/toruwalt/hng12-backend-stage0"
            }

    return jsonify(info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
