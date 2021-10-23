from flask import Flask, jsonify
import time
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    dt=datetime.now()
    return jsonify({"time of Call": dt.strftime("%m/%d/%Y, %H:%M:%S")})

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)