from bottle import Bottle, run, \
     template, debug, static_file, request, post

import os, sys
import requests
import json
from inspect import getsourcefile
from os.path import abspath

import re

from gevent import monkey; monkey.patch_all()


dirname = os.path.dirname(abspath(getsourcefile(lambda:0)))

app = Bottle()
debug(True)


@app.route('/', method='POST')
def test():
    username = request.forms.get('username')
    print(username)

    response = requests.get("api-address")
    #response = '{"intent": {"confidence": 0.5}}'
    jsonObj = json.loads(response)
    #print(moi['intent']['confidence'])
    receivedThreshold = jsonObj['intent']['confidence']
    
    if (receivedThreshold > THRESHOLD):
      if (jsonObj['intent']['name'] == 'coursepoints'):
         
    else:
      callCSClient()
    
run(app, host='localhost', port=8080)
