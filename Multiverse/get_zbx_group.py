#!/bin/env python2.6
import os
import json
import multiverse_connect as m

def get_group(token, hostname):
    hostid = json.loads(m.connect({"jsonrpc": "2.0","method": "host.get","params": {"output": "extend","filter": {"host": [ "napsao-nix-zbx-proxy-1.vmcommerce.intra" ]}},"auth": token,"id":"1"}))['result'][0]['hostid']
    hostgroup = json.loads(m.connect({"jsonrpc": "2.0", "method": "hostgroup.get", "params": {"output": "extend", "hostids": hostid},"auth": token,"id":"1"}))['result'][0]['name']  
    return hostgroup
