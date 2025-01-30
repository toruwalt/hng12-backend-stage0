#!/usr/bin/python3
"""HNG Backend Stage 0"""

from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime
from datetime import datetime, timezone

app = Flask(__name__)
CORS(app)

#Info Details
email = "toruwalt1997@gmail.com"
github_url = "https://github.com/toruwalt/hng12-backend-stage0"

#Disable Python Dictionary Key sorting
app.json.sort_keys = False

@app.route("/")
def display_info():
    info = {
            "email": email,
            "current_datetime": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "github_url": github_url
            }

    return jsonify(info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
