from bottle import Bottle, run, \
     template, debug, static_file, request, post

import os, sys
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

run(app, host='localhost', port=8080)
