import requests
import json

'''

author: Dennis Hsieh
date: 11/13/2023



'''

'''

author: Dennis Hsieh
date: 11/13/2023

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


def get_parts(auth_toke, courseId, assignmentId):

    url = f"https://api.vocareum.com/api/v2/courses/{courseId}/assignments/{assignmentId}/parts"

    headers = {'Authorization':f"Token {auth_toke}"}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f'Unable to get students: {response.status_code}')
        return

    response_dict = json.loads(response.text)

    try:

        assignments = {}  # store assignments with key: id and value: assignment objects




    except KeyError:
        print('issue reading parts')
        return

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

