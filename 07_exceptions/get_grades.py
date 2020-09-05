# get_grades.py

def get_grades(fname):
    try:
        grades_file = open(fname, 'r')
    except IOError:
        raise ValueError('get_grades could not open ' + fname)
    grades = []
    for line in grades_file:
        try:
            grades.append(float(line))
        except:
            raise ValueError('Unable to convert line to flaot')
    return grades


def test_get_grades():
    try:
        grades = get_grades('input/quiz_grades.txt')
        grades.sort()
        median = grades[len(grades)//2]
        print('Median grade is', median)
    except ValueError as error:
        print('Whoops...', error)


if __name__ == '__main__':
    test_get_grades()