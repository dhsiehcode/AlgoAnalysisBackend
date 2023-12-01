import base64
import io
import os

import requests
import json
import zipfile

from flaskr import voc_objects

'''

author: Dennis Hsieh
date: 11/13/2023

'''

'''

gets all the assignments in a course given the id. returns a list of assignment objects

'''
def get_assignments(auth_token, courseId):

     url = f"https://api.vocareum.com/api/v2/courses/{courseId}/assignments"

     headers = {"Authorization": f"Token {auth_token}"}

     response = requests.get(url, headers=headers)

     if response.status_code != 200:
         print(f'Unable to get assignments: {response.status_code}')
         return

     response_dict = json.loads(response.text)

     try:

        ## gets all the assignments
        assignments = []
        for assignment_dict in response_dict['assignments']:
            assignment = voc_objects.Assignment(assignment_dict['name'], assignment_dict['id'])

            parts = get_parts(auth_token, courseId, assignment.get_id())
            assignment.set_parts(parts)
            assignments.append(assignment)

     except KeyError:
         print('issue reading assignments')
         return

     return assignments

'''

returns assignment object with name, id, and parts populated as a list of part objects

'''
def get_assignment(auth_token, courseId, assignmentId):
    url = f"https://api.vocareum.com/api/v2/courses/{courseId}/assignments/{assignmentId}"

    headers = {"Authorization": f"Token {auth_token}"}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f'Unable to get assignments: {response.status_code}')
        return

    response_dict = json.loads(response.text)

    try:


        assignment_dict =  response_dict['assignments']
        assignment = voc_objects.Assignment(assignment_dict['name'], assignment_dict['id'])

        parts = get_parts(auth_token, courseId, assignmentId)
        assignment.set_parts(parts)


    except KeyError:
        print('issue reading assignments')
        return

    return assignment


'''

returns a list of part objects given course id and assignment id

'''
def get_parts(auth_token, courseId, assignmentId):

    url = f"https://api.vocareum.com/api/v2/courses/{courseId}/assignments/{assignmentId}/parts"

    headers = {'Authorization':f"Token {auth_token}"}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f'Unable to get students: {response.status_code}')
        return

    response_dict = json.loads(response.text)

    parts = []

    try:

        for part in response_dict['parts']:

            part_id = part['id']
            part_name = part['name']

            parts.append(voc_objects.Part(part_name, part_id))

    except KeyError:
        print('issue reading parts')
        return

    return parts

'''

returns a Part object given the course id, assigment id, part id

'''
def get_part(auth_token, courseId, assignmentId, partId):



    url = f"https://api.vocareum.com/api/v2/courses/{courseId}/assignments/{assignmentId}/parts/{partId}"

    headers = {'Authorization':f"Token {auth_token}"}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f'Unable to get students: {response.status_code}')
        return

    response_dict = json.loads(response.text)

    part = voc_objects.Part(name=response_dict['parts']['name'], id = response_dict['parts']['id'])

    ## returns part object

    return part

'''

extracts submission of student to {save_location}/{zipfile_name}

returns the location where the code is and the inner directory specified by "dirname":"{string}


'''
def get_latest_submission(auth_token, courseId, assignmentId, partId, userId, save_location):

    url = f"https://api.vocareum.com/api/v2/courses/{courseId}/assignments/{assignmentId}/parts/{partId}/submissions/{userId}"

    headers = {"Authorization":f"Token {auth_token}"}

    response = requests.get(url, headers=headers)

    if response.status_code == 404:
    ## case where student doesn't have submission
        print("no assignments")
        return None, None

    if response.status_code != 200:
        print(f'Unable to get assignen: {response.status_code}')
        return

    response_dict = json.loads(response.text)

    if response_dict['status'] != "success":
        print("failed to read submission")
        return



    '''
    dict of format:
     {"userid":"{number}","partid":"{number}","last_submission_at":"{Month} {day} {year} {hour}:{minute}:{seconds}pm/am
        PST","submission_count":"{number}","dirname":"{string}","zipfilecontent":"{string}"}
    '''
    submission_info = response_dict['submissions'][0]

    content = submission_info['zipfilecontent']
    content = content.replace("\\", "")
    content_64 = base64.b64decode(content)

    zipfile_name = f"{userId}_submission"

    with open(f"{save_location}/{zipfile_name}.zip", "wb") as f:
        f.write(content_64)

    z = zipfile.ZipFile(f"{save_location}/{zipfile_name}.zip", "r")
    z.extractall(path=f"{save_location}")

    sub = voc_objects.Submission(userId, f"{save_location}/{submission_info['dirname']}", submission_info['last_submission_at'])


    return sub




'''

gets all the students in a particular course

auth_token: authentication token generated
courseId: the id of the course which we want to get the students in

'''
def get_students(auth_token, courseId):

    url = f"https://api.vocareum.com/api/v2/courses/{courseId}/users"

    headers = {"Authorization":f"Token {auth_token}"}

    #payload = {"role":""}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f'Unable to get students: {response.status_code}')
        return

    response_dict = json.loads(response.text)

    try:

        students = [] # store courses with id and name. students[n][0] = {name} students[n][1] = {id}

        for student in response_dict['users']:

            students.append(voc_objects.Student(student['name'], student['id']))


    except KeyError:
        print('issue reading students')
        return

    return students


'''
gets all the current courses that exists with its id and name
auth_token: authentication token generated

'''
def get_courses(auth_token):

    print("getting courses")

    url = "https://api.vocareum.com/api/v2/courses"

    headers = {"Authorization": f"Token {auth_token}"}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f'Unable to get courses: {response.status_code}')
        return

    response_dict = json.loads(response.text)

    try:

        courses = []

        for course_dict in response_dict['courses']:

            course = voc_objects.Course(course_dict['name'], course_dict['id'])

            course.set_assignments(get_assignments(auth_token, course.get_id()))

            courses.append(course)


    except KeyError:
        print('issue reading courses')
        return

    return courses

'''

returns and object representing a course with assignments populated

'''
def get_course(auth_token, courseId):

    url = f"https://api.vocareum.com/api/v2/courses/{courseId}"

    headers = {"Authorization": f"Token {auth_token}"}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f'Unable to get courses: {response.status_code}')
        return

    response_dict = json.loads(response.text)

    course_dict = response_dict['courses']

    course = voc_objects.Course(response_dict['name'], course_dict['id'])

    course.set_assignments(get_assignments(auth_token, courseId))

    return course

## Using Dennis' auth token for now
auth_toke = 'b7ced88c162ce28340e00851f5a216f4259e69c6'



'''

basic initialization to make sure we have the folder to store the submissions the way we want

'''
def init_check():

    if not os.path.exists(f"{os.getcwd()}/../submissions"):
        os.mkdir(f"{os.getcwd()}/../submissions")

'''

gets all the submissions of all students for an assignment in a course 

'''
def get_all_submissions_by_assignment(courseId,assignmentId):

    ## before db is up we get all students

    os.chdir("..")

    for partId, part in get_parts(auth_token=auth_toke, courseId=courseId, assignmentId=assignmentId).items():

        get_all_submissions_by_part(courseId=courseId, assignmentId=assignmentId, partId = partId)


'''

gets all the submissions from all students for a particular part of an assignment of a course

'''
def get_all_submissions_by_part(courseId, assignmentId, partId):

    ## before db is up we get all students

    students = get_students(auth_token=auth_toke, courseId=courseId)
    ## change working directory
    #cur_dir = os.curdir
    #os.chdir("..")

    try:

        os.makedirs((f"{os.getcwd()}/submissions/{courseId}/{assignmentId}/{partId}"))

    except OSError:
        None

    save_path = f"{os.getcwd()}/submissions/{courseId}/{assignmentId}/{partId}"


    for id, student in students.items():
        print(id, student)
        code_dir, inside_dir = get_latest_submission(auth_token=auth_toke, courseId=courseId, assignmentId=assignmentId, partId=partId, userId=id, save_location=save_path)

        if code_dir == None:
            continue

        print(code_dir)
        print(inside_dir)

        os.rename(f"{code_dir}\{inside_dir}", f"{code_dir}\{id}") ## rename the inside directory to be the sudent's id

    ## must return to directy of file
    #os.chdir(cur_dir)

    return save_path ## save path should now have all the files
