#!/bin/env python2.6
import os
import json
import multiverse_connect as m

def get_group(token, hostname):
    hostgroup = []
    hostid = json.loads(m.connect({"jsonrpc": "2.0","method": "host.get","params": {"output": "extend","filter": {"host": [ hostname ]}},"auth": token,"id":"1"}))['result'][0]['hostid']
    raw_hostgroup = json.loads(m.connect({"jsonrpc": "2.0", "method": "hostgroup.get", "params": {"output": "extend", "hostids": hostid},"auth": token,"id":"1"}))['result']
    for host_group in raw_hostgroup:
        hostgroup.append(host_group.get('name'))
    return hostgroup
