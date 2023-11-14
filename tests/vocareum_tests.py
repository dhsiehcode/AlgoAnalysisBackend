
from flaskr import vocareum

auth_token = "b7ced88c162ce28340e00851f5a216f4259e69c6"

course_id = '101632' # id for automatic runtime analysis



## passed
def test_get_courses():

    print(vocareum.get_courses(auth_token))

## passed
def test_get_students():

    print(vocareum.get_students(auth_token, course_id))

