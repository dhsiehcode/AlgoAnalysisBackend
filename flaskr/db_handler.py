import sqlite3
from flask import current_app, g, Blueprint, request
import requests
from flaskr import vocareum
from flaskr import db
from flask import Flask

'''


'''

bp = Blueprint('info', __name__, url_prefix='/info')


@bp.route('/get', methods = ["GET"])
def get_info():
    conn = db.get_db()
    courses = conn.execute('SELECT * FROM courses').fetchall() ## dict of {}
    users = conn.execute("SELECT * FROM users").fetchall() ## dict of {}
    assignments = conn.execute("SELECT * FROM assignments").fetchall() ## dict of {}
    parts = conn.execute("SELECT * FROM parts").fetchall() ## dict of {}

    '''
    
    testing to prove this functionality works
    
    '''

    users_output = "users: "

    for user in users:
        users_output += f" {user['name']} with id {user['id']} in course {user['courseId']}"

    assignment_output = "assignments: "

    for assignment in assignments:
        assignment_output += f" {assignment['name']} with id {assignment['id']} in course {assignment['courseId']}"

    part_output = "parts: "

    for part in parts:
        part_output += f" {part['name']} with id {part['id']} in course {part['courseId']} in assignment {part['assignmentId']}"

    db.close_db()

    return users_output + " \n " + assignment_output + " \n " + part_output





@bp.route('/update', methods = ["GET"])
def update_info():
    auth_token = 'b7ced88c162ce28340e00851f5a216f4259e69c6'

    conn = db.get_db()

    courses = vocareum.get_courses(auth_token) ## course a list of course objects

    ## check if exist courses
    for course in courses:
        conn.execute("INSERT INTO courses (id, name) VALUES (?, ?)", (course.get_id(), course.get_name()))





@bp.route('/populate', methods = ["GET"])
def populate_info():
    auth_token = 'b7ced88c162ce28340e00851f5a216f4259e69c6'

    conn = db.get_db()

    courses = vocareum.get_courses(auth_token) ## course a list of course objects

    ## populate courses
    for course in courses:

        if conn.execute("SELECT EXISTS(SELECT * FROM courses WHERE id = ? AND name = ?)", (course.get_id(), course.get_name(),)):
            continue
        else:
            conn.execute("INSERT INTO courses (id, name) VALUES (?, ?)", (course.get_id(), course.get_name()))

    ### populate students and course hey are in

    for course in courses:

        for student in vocareum.get_students(auth_token, course.get_id()):

            if conn.execute("SELECT EXISTS(SELECT * FROM users WHERE id = ? AND name = ? AND courseId = ?)",
                            (student.get_id(), student.get_name(), course.get_id(),)):
                continue
            else:
                conn.execute("INSERT INTO users (id, name, courseId) VALUES (?, ?, ?)", (student.get_id(), student.get_name(), course.get_id()))

    ### populate assignment

    for course in courses:

        for assignment in course.get_assignments():

            if conn.execute("SELECT EXISTS(SELECT * FROM assignments WHERE id = ? AND name = ? AND courseId = ?)",
                            (assignment.get_id(), assignment.get_name(), course.get_id())):
                continue
            else:
                conn.execute("INSERT INTO assignments (id, name, courseId) VALUES (?, ?, ?)", (assignment.get_id(), assignment.get_name(), course.get_id()))

            ## populate part

            for part in assignment.get_parts():

                if conn.execute("SELECT EXISTS(SELECT * FROM parts WHERE id = ? AND name = ? AND assignmentId = ? AND courseId = ?)",
                                (part.get_id(), part.get_name(), assignment.get_id, course.get_id())):
                    continue
                else:
                    conn.execute("INSERT INTO parts (id, name, assignmentId, courseId) VALUES (?, ?, ?, ?)", (part.get_id(), part.get_name(), assignment.get_id(), course.get_id()))

    conn.commit()
    users = conn.execute(
        'SELECT * FROM users '
    ).fetchall()

    db.close_db()

    ''' 
    the following lines test the functionality
    '''

    print("getting users as proof of function")

    for user in users:
        print(user['name'])




    return "updated successfully"




#with app.app_context():
    #populate_info(auth_token)
