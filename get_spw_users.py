#!/usr/bin/python
import xmlrpclib
import multiverse_config as config

client = xmlrpclib.Server(config.connect['spw_server'], verbose=0)

key = client.auth.login(config.login['spw_user'], config.login['spw_password'] )

list = client.user.list_systems(key)

for system in list:
       print system.get('system')
client.auth.logout(key)
