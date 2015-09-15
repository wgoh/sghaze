#!flask/bin/python
import os
import sys
from flask import Flask
from pymongo import MongoClient
import json
from bson import BSON
from bson import json_util
import argparse

PORT = 80

client = MongoClient()
db = client.haze

app = Flask(__name__)

@app.route('/')
def index():
    records = db.psi.find().sort("timestamp",-1).limit(20)
    obj = [json.dumps(r, sort_keys=True, indent=4, default=json_util.default) for r in records]
    res = "[" + ",".join(obj) + "]"
    return res

if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) == 2 else ''
    if target == 'dev':
        app.run(debug=True,port=PORT)
    else:
        app.run(debug=True, host='0.0.0.0',port=PORT)

