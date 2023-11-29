
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

    def __init__(self, name, id):
        self.courseId = id
        self.name = name
        self.assignments = []

    def get_course(self):
        return self.name

    def get_id(self):
        return self.id

    def add_assignment(self, assignment):
        self.assignments.append(assignment)

    def get_assignments(self):
        return self.assignments

    def set_assignments(self, assignments):
        self.assignments = assignments



