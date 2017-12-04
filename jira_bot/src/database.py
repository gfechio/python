import _mysql

import config

db = _mysql.connect(host=config.db['server'],      # your host, usually localhost
                     user=config.db['user'],        # your username
                     passwd=config.db['password'],  # your username
                     db="office")                   # name of the data base

def insert(username, url):
    db.query("""INSERT query """)

def inactive(username, url):
    db.query("""UPDATE query""")

def show():
    db.query("""SELECT query""")

