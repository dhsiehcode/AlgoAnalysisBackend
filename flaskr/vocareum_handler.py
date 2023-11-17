import os
import vocareum




## Using Dennis' auth token for now
auth_toke = 'b7ced88c162ce28340e00851f5a216f4259e69c6'



'''

basic initialization to make sure we have the folder to store the submissions the way we want

'''
def init_check():

    if not os.path.exists(f"{os.getcwd()}/../submissions"):
        os.mkdir(f"{os.getcwd()}/../submissions")

def get_all_submissions_by_assignment(courseId,assignmentId):

    ## before db is up we get all students

    students = vocareum.get_students(auth_token=auth_toke, courseId=courseId)

    os.chdir("..")

    for partId, part in vocareum.get_parts(auth_token=auth_toke, courseId=courseId, assignmentId=assignmentId).items():

        get_all_submissions_by_part(courseId=courseId, assignmentId=assignmentId, partId = partId)


'''

gets all the submissions from all students for a particular part of an assignemnt of a course

'''
def get_all_submissions_by_part(courseId, assignmentId, partId):

    ## before db is up we get all students

    students = vocareum.get_students(auth_token=auth_toke, courseId=courseId)
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
        code_dir, inside_dir = vocareum.get_latest_submission(auth_token=auth_toke, courseId=courseId, assignmentId=assignmentId, partId=partId, userId=id, save_location=save_path)

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






