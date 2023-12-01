import base64
import gzip

import shutil

from flaskr import vocareum
import zipfile
import io

auth_token = "b7ced88c162ce28340e00851f5a216f4259e69c6"

course_id = '101632' # id for automatic runtime analysis



## passed
def test_get_courses():

    print(vocareum.get_courses(auth_token))

## passed
def test_get_students():

    print(vocareum.get_students(auth_token, course_id))

def test_get_submissions():

    vocareum.get_latest_submission(auth_token=auth_token, courseId= course_id, assignmentId= "2336373",  partId= "2336418", userId= "1584772", save_location='C:\Dennis\Purdue\Junior Year\Algorithm Analysis\AlgoAnalysisBackend\submissions' )


test_get_submissions()






