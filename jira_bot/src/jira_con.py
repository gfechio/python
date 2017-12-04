from jira import JIRA

import config

def connect():
    options = { 'server': "server"}
    jira = JIRA(options, basic_auth=(config.conn["user"], config.conn["password"]))
    return jira

def comment(issue, comment):
    jira = connect()
    jira.add_comment(issue, comment)

def transition_close(issue):
    jira = connect()
    jira.transition_issue(issue, '2', assignee={'name': config.conn["user"]}, resolution={'id': '3'})
