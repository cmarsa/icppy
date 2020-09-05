# grade_report.py
from Grades import Grades
from MITPerson import UG, Grad

def grade_report(course):
    '''Assumes course is of type Grades'''
    report = ''
    for s in course.get_students():
        total = 0.0
        num_grades = 0
        for grade in course.get_grades(s):
            total += grade
            num_grades += 1
        try:
            average = total / num_grades
            report = report + '\n' + str(s) + \
                '\'s mean grade is ' + str(average)
        except ZeroDivisionError:
            report = report + '\n' + \
                str(s) + ' has no grades.'
    return report


def test_grade_report():
    ug1 = UG('Jane Doe', 2014)
    ug2 = UG('John Doe', 2015)
    ug3 = UG('David Henry', 2003)
    g1 = Grad('Billy Buckner')
    g2 = Grad('Bucky F. Dent')
    six_hundred = Grades()
    six_hundred.add_student(ug1)
    six_hundred.add_student(ug2)
    six_hundred.add_student(g1)
    six_hundred.add_student(g2)
    for s in six_hundred.get_students():
        six_hundred.add_grade(s, 75)
    six_hundred.add_grade(g1, 25)
    six_hundred.add_grade(g2, 100)
    six_hundred.add_student(ug3)
    print(grade_report(six_hundred))


if __name__ == '__main__':
    test_grade_report()