import os

conn = dict(
    server = 'servers',
    user = os.environ['CONN_USER'],
    password = os.environ['CONN_PW']
    )
db = dict(
    server = 'database',
    user = os.environ['DB_USER'],
    password = os.environ['DB_PW']
)
info = dict(
    project = "SQUID",
    ticket_status = "Open",
    summary_index = "(squid)"
    )
puppet = dict(
    server = "PUppetize",
    dir = "/puppet/modules/squid/files",
    file = "blacklist"
    )
servers = dict(
    squid = [
    "Server1"
    "Server2"
    ],
)
