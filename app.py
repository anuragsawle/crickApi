from flask import Flask, jsonify
from pycricbuzz import Cricbuzz

app = Flask(__name__)


@app.route('/', methods=['GET'])
def helloworld():
    c = Cricbuzz()
    matches = c.matches()
    d = []
    for match in matches:
        d.append(match)
    return jsonify(d)
