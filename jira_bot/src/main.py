#!/usr/bin/python

# -*- coding: latin-1 -*-

import datetime
import sys

from jira import JIRA

import logging
import config
import runner
import jira_con

def get_issues():
    connect = jira_con.connect()
    jra = connect.project("SQUID")
    issues_proj = connect.search_issues('project=SQUID')
    return issues_proj

def tasks_parser():
    issues = get_issues()
    connect = jira_con.connect()
    for issue in issues:
        if str(issue.fields.status) == config.info["ticket_status"] and config.info["summary_index"] in str(issue.fields.summary) and issue.fields.description:
            sys.stdout.write("Reading the "+str(issue)+" : "+str(issue.fields.summary)+"\n")
            last_line = issue.fields.description.split("#")[-1]
            if "Bot" in last_line:
                sys.stdout.write("Bot job found at "+str(issue)+"\n") 
                jira_con.comment(issue, "Bot working on ticket")
                work = str(last_line.split(":")[1].lower())
                func_options = last_line
                try:
                    getattr(runner,"%s" %work)(func_options, issue, str(issue.fields.summary))
                except:
                    jira_con.comment(issue, "Are you using the right tag ? \n Example: \n #Bot:Command:URL = url.com, url.com")
            else:
                sys.stdout.write("Bot did not found new ticktes to work\n") 


tasks_parser()
try:
    if __name__ == "__main__":
        tasks_parser()
except:
    sys.stderr.write("Could not call main function!!\n")
