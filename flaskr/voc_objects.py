
'''

author: Dennis Hsieh
11/28/2023

wrapper class for some vocareum objeccts

'''


'''
represents a student 
'''
class Student:

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_name(self):

        return self.name

    def get_id(self):

        return self.id

class Instructor:

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

class TA:

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id



'''

represents a part in an assignment takes the name and id for the part
'''
class Part:

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_name(self):

        return self.name

    def get_id(self):

        return self.id


'''
represents and assignment in a course
takes in id and name
parts is a list that stores parts of the assignment
'''
class Assignment:

    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.parts = []

    def get_name(self):

        return self.name

    def get_id(self):

        return self.id

    def add_part(self, part):

        self.parts.append(part)

    def get_parts(self):

        return self.parts

    def set_parts(self, parts):

        self.parts = parts



'''

object that represents a course in vocareum
represents and assignment in a course
takes in id and name
assignments is a list that stores assignments of the course
'''
class Course:

    def __init__(self, name, id, term):
        self.id = id
        self.name = name
        self.assignments = []
        self.term = term

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def add_assignment(self, assignment):
        self.assignments.append(assignment)

    def get_assignments(self):
        return self.assignments

    def set_assignments(self, assignments):
        self.assignments = assignments

    def get_term(self):
        return self.term

    def get_unique_name(self):

        return self.term + self.name

    def get_assignment_names(self):

        output = ""

        for assignment in self.assignments:
            for part in assignment.parts:
                output += (assignment.get_name() + part.get_name())
                output += ","

        return output

    def get_vocareum_ids(self):

        output = ""

        for assignment in self.assignments:
            for part in assignment.get_parts():
                output += f"a{assignment.get_id()}_p{part.get_id()}"
                output += ","

        return output


'''

wrapper object that represents a submission dwonload on vocareum

'''
class Submission:

    def __init__(self, id, name, dir_name, time_stamp, submission_count = 1):
        self.id = id
        self.name = name
        self.dir_name = dir_name
        self.last_sub = time_stamp
        self.sub_count = submission_count

    def get_user(self):
        return self.name

    def get_stored_dir(self):
        return self.dir_name

    def get_sub_time(self):
        return self.last_sub

    def get_sub_count(self):
        return self.sub_count


