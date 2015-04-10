#!/bin/env python2.6
import os
import json
import urllib
import urllib2
import sys
import fcntl
import string
import subprocess
import multiverse_config as config

#Define to connect into server and send json payload
def connect(data):
    data_json = json.dumps(data)
    payload = urllib2.Request(config.connect['zbx_server'], data_json, {'Content-Type': 'application/json'})
    res = urllib2.urlopen(payload)
    response = res.read()
    return response

# Zabbix store Token
def get_token():
    response = connect({ "jsonrpc":"2.0","method":"user.login","params":{"user": config.login['zbx_user'],"password": config.login['zbx_password']}, "id":"1" })
    token = json.loads(response)['result']
    return token

