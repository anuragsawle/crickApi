from flask import Flask, jsonify
from pycricbuzz import Cricbuzz

app = Flask(__name__)


@app.route('/', methods=['GET'])
def getMatches():
    c = Cricbuzz()
    matches = c.matches()
    a = []
    for match in matches:
        d = {'series': match['srs'],
             'team1': match['team1']['name'],
             'team2': match['team2']['name'],
             'status': match['status']}
        a.append(d)
    return jsonify(a)
