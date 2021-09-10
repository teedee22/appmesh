import random
from datetime import datetime
import time

from flask import Flask, jsonify, request, json

app = Flask(__name__)


@app.route("/new", methods=['GET'])
def new():
    timestart = datetime.now()

    number = random.randint(1, 100) / 100
    print(f"Call will take {number} seconds")
    time.sleep(number)
    timeend = datetime.now()

    timetaken = round((timeend - timestart).total_seconds(), 3)
    print(f"Call complete, system took {timetaken} to complete")
    payload = {"message": f"call took v2 {timetaken} seconds"}
    return jsonify(payload)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
