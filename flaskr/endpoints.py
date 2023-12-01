import os
import sqlite3
from flask import current_app, g, Blueprint, request
import requests
from flaskr import vocareum
from flaskr import db
from flask import Flask

'''
author: Dennis

should have most endpoints here

TODO:
1. endpoints to download submissions 
    1-1 error handling to make sure we don't re-download code that hasn't bee changed
    1-2 download according to specification such as course, assignment, part

2. endpoints to run submission
    2-1 future handling to bundle with downloading so code not changed doesn't get run twice
    2-2 run multiple tests on submission as desired by user
    2-3 return information desired by user (maybe can be handled on front-end)


 
'''

## sets up a blueprint so it can be called
bp = Blueprint('services', __name__, url_prefix='/services')

'''

will download EVERY SINGLE SUBMISSION. 
This means latest submission for every part in every assignment in every course for every student

'''
@bp.route("/download_submission/all", methods = ["GET"])
def download_submissions():
    auth_token = 'b7ced88c162ce28340e00851f5a216f4259e69c6'

    vocareum.init_check() ## makes sure directory exists

    conn = db.get_db()
    courses = conn.execute('SELECT * FROM courses').fetchall()  ## dict of {}


    for course in courses:

        download_submissions_course(courseId=course['id'])

    return "success"

@bp.route("/download_submission/part", methods = ["GET"])
def download_submissions_part(courseId = '', assignmentId = '', partId = ''):

    auth_token = 'b7ced88c162ce28340e00851f5a216f4259e69c6'
    courseId = '101632'
    assignmentId = '2336373'
    partId = '23336418'

    vocareum.init_check()

    conn = db.get_db()

    users = conn.execute("SELECT * FROM users WHERE courseId = ?", (courseId, )).fetchall()
    part = conn.execute("SELECT * FROM parts WHERE id = ? AND courseId = ? AND assignmentId = ? ", (partId, courseId, assignmentId, )).fetchall()

    save_path = f"{os.getcwd()}/submissions/{courseId}/{assignmentId}/{part['id']}"
    os.makedirs(save_path)

    for user in users:
        last_sub = vocareum.get_latest_submission(auth_token, courseId, assignmentId, partId, user['id'],
                                                  save_path)

    return "success"



@bp.route("/download_submission/assignment", methods = ["GET"])
def download_submissions_assignment(courseId = None, assignmentId = ''):

    if courseId is None:
        courseId = '101632'
    assignmentId = '2336373'

    auth_token = 'b7ced88c162ce28340e00851f5a216f4259e69c6'

    vocareum.init_check()

    conn = db.get_db()

    users = conn.execute("SELECT * FROM users WHERE courseId = ?", (courseId, )).fetchall()  ## dict of {}
    assignment = conn.execute("SELECT * FROM assignments WHERE courseId = ?  AND id = ? ", (courseId, assignmentId, )).fetchone()  ## dict of {}

    parts = conn.execute("SELECT * FROM parts WHERE courseId = ? AND assignmentId = ? ", (courseId, assignmentId, )).fetchall()

    for part in parts:
        save_path = f"{os.getcwd()}/submissions/{courseId}/{assignmentId}/{part['id']}"
        os.makedirs(save_path)

        for user in users:

            last_sub = vocareum.get_latest_submission(auth_token, courseId, assignment['id'], part['id'], user['id'],
                                                  save_path)

    return "success"


@bp.route("/download_submission/course", methods = ["GET"])
def download_submissions_course(courseId = None):


    if courseId is None:
        print(courseId)
        courseId = '101632'

    auth_token = 'b7ced88c162ce28340e00851f5a216f4259e69c6'

    vocareum.init_check()

    conn = db.get_db()

    course = conn.execute('SELECT * FROM courses WHERE id = ?', (courseId, )).fetchone()  ## dict of {}
    users = conn.execute("SELECT * FROM users WHERE courseId = ?", (courseId, )).fetchall()  ## dict of {}
    assignments = conn.execute("SELECT * FROM assignments WHERE courseId = ?", (courseId, )).fetchall()  ## dict of {}

    for assignment in assignments:

        parts = conn.execute("SELECT * FROM parts WHERE courseId = ? AND assignmentId = ?", (courseId, assignment['id'],)).fetchall()  ## dict of {}

        for part in parts:
            save_path = f"{os.getcwd()}/submissions/{courseId}/{assignment['id']}/{part['id']}"
            os.makedirs(save_path)



    for user in users:

        for assignment in assignments:

            parts = conn.execute("SELECT * FROM parts WHERE courseId = ? AND assignmentId = ?",
                                 (courseId,assignment['id'],)).fetchall()  ## dict of {}
            for part in parts:

                save_path = f"{os.getcwd()}/submissions/{courseId}/{assignment['id']}/{part['id']}"

                last_sub = vocareum.get_latest_submission(auth_token, course['id'], assignment['id'], part['id'], user['id'], save_path)




    return "success"




@bp.route("/download_submission/student", methods = ["GET"])
def download_submissions_student(userId = ''):

    auth_token = 'b7ced88c162ce28340e00851f5a216f4259e69c6'

    vocareum.init_check()

    conn = db.get_db()

    users = conn.execute("SELECT * FROM users").fetchall()  ## dict of {}

    if not userId in users['id']:
        return ## student doesn't exist

    courses = conn.execute('SELECT * FROM users WHERE id = ?', (userId,)).fetchall()  ## dict of {}

    for course in courses:

        assignments = conn.execute("SELECT * FROM assignments WHERE courseId = ?", (course['id'])).fetchall()  ## dict of {}

        for assignment in assignments:

            parts = conn.execute("SELECT * FROM parts WHERE courseId = ? AND assignmentId = ?", (course['id'], assignment['id']))

            for part in parts:
                save_path = f"{os.getcwd()}/submissions/{course['id']}/{assignment['id']}/{part['id']}"
                os.makedirs(save_path)

                last_sub = vocareum.get_latest_submission(auth_token, course['id'], assignment['id'], part['id'], userId, save_path)


    return "success"




