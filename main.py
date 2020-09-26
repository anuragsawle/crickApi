from flask import Flask, jsonify
from pycricbuzz import Cricbuzz

app = Flask(__name__)


@app.route('/', methods=['GET'])
def getMatches():
    d={'name':'Anurag'}
    return jsonify(d)
