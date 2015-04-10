#!/usr/bin/python
import xmlrpclib
import json
import get_zbx_group as zg
import multiverse_connect as m
import multiverse_config as config

def get_hostname():
    server = xmlrpclib.Server(config.connect['spw_server'], verbose=0)
    auth = server.auth.login(config.login['spw_user'], config.login['spw_password'] )
    
    group_list = []
    group_check = server.systemgroup.listAllGroups(auth)
    for raw_group in group_check:
        group_list.append(raw_group.get('name'))
    
    host_list = [] 
    host_list = server.system.listSystems(auth)
    for system in host_list:
        hostname = system.get('name')
        token = m.get_token()
        hostgroup = zg.get_group(token, hostname)
        if hostgroup not in group_list:
            c_hostgroup = server.systemgroup.create(auth, hostgroup, hostgroup)

    server.auth.logout(auth)

get_hostname()
