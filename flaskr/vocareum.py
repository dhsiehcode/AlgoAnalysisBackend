import base64
import io
import os

import requests
import json
import zipfile

'''

author: Dennis Hsieh
date: 11/13/2023

'''

'''

gets all the assignments in a course given the id. returns 

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

         assignments = {}  # store assignments with key: id and value: assignment objects




     except KeyError:
         print('issue reading assignments')
         return



'''

gets all the parts that exists in a assignment

'''
def get_parts(auth_token, courseId, assignmentId):

    url = f"https://api.vocareum.com/api/v2/courses/{courseId}/assignments/{assignmentId}/parts"

    headers = {'Authorization':f"Token {auth_token}"}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f'Unable to get students: {response.status_code}')
        return

    response_dict = json.loads(response.text)

    parts = {}

    try:

          # store assignments with key: id and value: part name

        for part in response_dict['parts']:

            parts[part['id']] = part['name']

    except KeyError:
        print('issue reading parts')
        return

    return parts


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


    return f"{save_location}", submission_info['dirname']




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

        students = {} # store courses with key: id and value: student

        for student in response_dict['users']:
            students[student['id']] = student['name']

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

        courses = {} # store courses with key: id and value: course name

        for course in response_dict['courses']:
            courses[course['id']] = course['name']

    except KeyError:
        print('issue reading courses')
        return

    return courses

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

    students = get_students(auth_token=auth_toke, courseId=courseId)

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

#get_all_submissions_by_part(courseId='101632', assignmentId='2336373', partId='2336418')

get_all_submissions_by_assignment(courseId='101632', assignmentId='2336373')