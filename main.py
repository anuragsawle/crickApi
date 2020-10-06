from flask import Flask, jsonify
from pycricbuzz import Cricbuzz

app = Flask(__name__)

#Return the Live score in json format
@app.route('/', methods=['GET'])
def getMatches():
    matches = Cricbuzz().matches()
    d=matches
    A="hello world"
    return jsonify(d)

if __name__ == "__main__":
    app.run(debug=TRUE)
