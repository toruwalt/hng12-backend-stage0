#!/usr/bin/python3
"""HNG Backend Stage 0"""

from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime
from datetime import datetime, timezone

app = Flask(__name__)
CORS(app)

# Get current time in UTC
current_time_utc = datetime.now(timezone.utc)

# Format as ISO 8601 with 'Z' at the end
iso_format_with_z = current_time_utc.strftime("%Y-%m-%dT%H:%M:%SZ")

print(iso_format_with_z)

@app.route("/", methods=['GET'])
def display_info():
    info = {
            "email": "toruwalt1997@gmail.com",
            "current_datetime": iso_format_with_z,
            "github_url": "https://github.com/toruwalt/hng12-backend-stage0"
            }

    return jsonify(info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
