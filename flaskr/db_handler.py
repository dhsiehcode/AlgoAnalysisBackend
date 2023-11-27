import sqlite3
from flask import current_app, g
import requests
import db


'''


'''

@app.route('/get_info/', methods = ("GET"))
def get_info():
    conn = db.get_db()
    courses = conn.execute('SELECT * FROM courses') ## dict of {}
    users = conn.execute("SELECT * FROM users") ## dict of {}
    assignments = conn.execute("SELECT * FROM assignments") ## dict of {}
    parts = conn.execute("SELECT * FROM parts") ## dict of {}



@app.route('/update_info/')


