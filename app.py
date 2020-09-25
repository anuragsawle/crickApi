from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/',methods=['GET'])
def helloworld():
    d={}
    d['msg']='Hello World'
    return jsonify(d)

if __name__ =='__main__':
    app.run(debug=True)
