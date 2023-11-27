import sqlite3

import click
from flask import current_app, g

'''

author: Dennis Hsieh
date: 11/10/2023

database setup file
I'm assuming that database will store the most recent runtime profile for student's code
Also should store some basic information about students

'''

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db() # returns database connection

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

def get_db_connection():
    db = get_db()
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.row
    return conn

