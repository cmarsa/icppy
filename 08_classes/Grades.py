# Grades.py

class Grades:
    '''
    '''
    def __init__(self):
        '''Create empty grade book'''
        self.students = []
        self.grades = {}
        self.is_sorted = True
    
    def add_student(self, student):
        '''
        Assumes student is of type Student
        Add student to the grade book
        '''
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.get_id()] = []
        self.is_sorted = False
    
    def add_grade(self, student, grade):
        '''
        Assumes: grade is a float
        Add grade to the list of grades for student
        '''
        try:
            self.grades[student.get_id()].append(grade)
        except:
            raise ValueError('Student not in mapping')
    
    def get_grades(self, student):
        '''
        Return a list of grades for student
        '''
        try:
            return self.grades[student.get_id()][:]
        except:
            raise ValueError('Student not in mapping')
    
    def get_students(self):
        '''
        Return the students in the grade book one at a time
        in alphabetical order
        '''
        if not self.is_sorted:
            self.students.sort()
            self.is_sorted = True
        for s in self.students:
            yield s
