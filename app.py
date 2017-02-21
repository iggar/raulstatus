import datetime
import flask
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import json
import os
import pickle
import sys

app = Flask(__name__)
CORS(app)

now = datetime.datetime.now()

#server initialisation
raulStatus = {
    'open': False,
    'date-time': now.isoformat(),
    'user': u'Raul Seixas'
}

pickle.dump(raulStatus, open( "save.p", "wb" ) )

@app.route('/status/', methods=['GET'])
def get_items():
    return jsonify(raulStatus)


@app.route('/status/checkin',methods=['POST'])
def check_in():
    raulStatus['open'] = True
    now = datetime.datetime.now()
    raulStatus['date-time']=now.isoformat()
    reqData = request.get_json(silent=True)
    if (reqData != None):
      raulStatus['user']=reqData['user']
    else:
      raulStatus['user']="Raul Seixas"
    pickle.dump(raulStatus, open( "save.p", "wb" ) )
    return jsonify(raulStatus)

@app.route('/status/checkout',methods=['POST'])
def check_out():
    raulStatus['open'] = False
    now = datetime.datetime.now()
    raulStatus['date-time']=now.isoformat()
    reqData = request.get_json(silent=True)
    if (reqData != None):
      raulStatus['user']=reqData['user']
    else:
      raulStatus['user']="Raul Seixas"
    pickle.dump(raulStatus, open( "save.p", "wb" ) )
    return jsonify(raulStatus)


@app.route("/")
def index():
    return "Hello, there's nothing for you here!"

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
