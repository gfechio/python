#!/usr/bin/python
# -*- coding: latin-1 -*-

import sys, os
import datetime
import random

import config 
import web_test
import system_test
import jira_con
import puppet_run as puppet
import database as db


def blacklist(options, issue, summary):
    options = options.split(":")[2]
    non_pci_server = config.servers["squid"] 
    vanIndex = random.randrange(0,len(non_pci_server))
    van_server = non_pci_server[vanIndex]
    sys.stdout.write("%s used as vanguard server "+van_server+"\n") 
    del non_pci_server[vanIndex]
    sys.stdout.write("Removing "+van_server+" from list (To not deploy twice)\n")
    
    for url in block_urls_parse(options):
        sys.stdout.write("Blocking folllowing URLs -> "+url) 
        jira_con.comment(issue,"Blocking folllowing URLs -> "+url)
        put_file = puppet.put_file(config.puppet["server"], config.conn["user"], config.conn["password"],config.puppet["dir"], config.puppet["file"], url) 

        if put_file == "OK":

            if db.insert(config.conn["user"], url) == "OK":
                system_test.run(van_server, config.conn["user"], config.conn["password"])
                web_test.run(van_server, url)

            else:
                jira_con.comment(issue, "Automation error, please check")
                db.inactive(config.conn["user"], url)
                sys.exit()

        elif put_file == "NOK":
            jira_con.comment(issue, "URL already blacklisted")
            jira_con.transition_close(issue)

        else:
            db.inactive(config.conn["user"], url)
            system_test.run(van_server, config.conn["user"], config.conn["password"])
            sys.stderr.write("Problem during execution please check!")
            jira_con.comment(issue, 'Problem during execution, bot could not solve') 

    jira_con.comment(issue, 'Tests passed successfully, applying to the pool')
    puppet.kick(config.puppet["server"], config.conn["user"], config.conn["password"])

    jira_con.comment(issue, 'Everything done closing ticket. Run puppet deploy manually')
    jira_con.transition_close(issue)


def block_urls_parse(urls):
    import re
    block_urls = [re.escape(urls.replace(" ",""))+"$\n" for urls in urls.split("=")[1].split(",")]
    return block_urls

def get_blacklist(options, issue, summary):
    import send_email
    import paramiko
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(van_server, username=config.conn["user"], password=config.conn["password"])
    sftp = ssh.open_sftp()
    f = sftp.open("/etc/squid/blacklist", 'r')
    send_email.send_email(f)
    jira_con.comment(issue, "Email sent to blacklist.url mail list")
    jira_con.transition_close(issue)
