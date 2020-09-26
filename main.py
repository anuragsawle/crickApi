from flask import Flask, jsonify
from pycricbuzz import Cricbuzz

app = Flask(__name__)


@app.route('/', methods=['GET'])
def getMatches():
    matches = Cricbuzz().matches()
    d=matches
    return jsonify(d)
