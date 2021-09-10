import requests
from flask import Flask, jsonify, request
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware

app = Flask(__name__)
plugins = ('ECSPlugin',)
xray_recorder.configure(plugins=plugins)
XRayMiddleware(app, xray_recorder)


@app.route("/mesh", methods=['GET'])
def new():
    url = "http://serviceb.apps.local/new"
    response = requests.get(url)
    return jsonify(response.text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
