import sqlite3
from sqlite3 import Error



def connect(db):
    """ Create a connection to the SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db)
        print(f'Database: {db}\n' +
              f'SQLite Version {sqlite3.version}')
        return conn
    except Error as e:
        print(e)

    return conn

def execute(conn, query):
    """ Execute a SQL query """
    try:
        c = conn.cursor()
        c.execute(query)
    except Error as e:
        print(e)

def init(db):
    """ Creates table structure for database. """
    conn = connect(db)

    execute(conn, """CREATE TABLE IF NOT EXISTS channel (
                          id integer PRIMARY KEY,
                          channel text NOT NULL,
                          type integer NOT NULL);""")
    execute(conn, """CREATE TABLE IF NOT EXISTS role (
                          id integer PRIMARY KEY,
                          name text NOT NULL,
                          rank text NOT NULL);""")
    execute(conn, """CREATE TABLE IF NOT EXISTS user (
                          id integer PRIMARY KEY,
                          user text NOT NULL,
                          name text NOT NULL,
                          join_date text NOT NULL,
                          rank text NOT NULL,
                          point integer NOT NULL,
                          win int NOT NULL,
                          loss integer NOT NULL,
                          draw integer NOT NULL);""")
    execute(conn, """CREATE TABLE IF NOT EXISTS match (
                          id integer PRIMARY KEY,
                          start text NOT NULL,
                          atk text NOT NULL,
                          def text NOT NULL);""")
    execute(conn, """CREATE TABLE IF NOT EXISTS history (
                          id integer PRIMARY KEY,
                          start text NOT NULL,
                          atk text NOT NULL,
                          def text NOT NULL,
                          end text NOT NULL,
                          winner text NOT NULL,
                          points integer NOT NULL);""")
    execute(conn, """CREATE TABLE IF NOT EXISTS log (
                          id integer PRIMARY KEY,
                          name text NOT NULL,
                          cmd text NOT NULL,
                          ok bool NOT NULL);""")
