# Person.py
import datetime

class Person:

    def __init__(self, name):
        '''Create a person'''
        self.name = name
        try:
            last_blank = name.rindex(' ')
            self.last_name = name[last_blank + 1:]
        except:
            self.last_name = name
        self.birthday = None
    
    def get_name(self):
        '''Returns self's full name'''
        return self.name
    
    def get_last_name(self):
        '''Returns self's last name'''
        return self.last_name
    
    def set_birthday(self, birthdate):
        '''
        Assumes birthdate is of type datetime.date
        Sets self's birthday to birthdate
        '''
        self.birthday = birthdate
    
    def get_age(self):
        '''Returns self's current age in days'''
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days
    
    def __lt__(self, other):
        '''
        Returns True if self precedes other in alphabetical order,
        and False otherwise. Comparison is based on last names, but if
        these are the same full names are compared.
        '''
        if self.last_name == other.last_name:
            return self.name < other.name
        return self.last_name < other.last_name
    
    def __str__(self):
        '''Returns selfs name'''
        return self.name


def test_person():
    me = Person('Michael Guttag')
    him = Person('Barack Hussein Obama')
    her = Person('Madonna')
    print(him.get_last_name())
    him.set_birthday(datetime.date(1961, 8, 4))
    her.set_birthday(datetime.date(1958, 8, 16))
    print(him.get_name(), 'is', him.get_age(), 'days old')

    # printing and sorting diff persons
    people = [me, him, her]
    print('\nPrinting people in inserted order:')
    for p in people:
        print(p)
    
    people.sort(reverse = True)
    print('\nPrinting people sorted:')
    for p in people:
        print(p)


if __name__ == '__main__':
    test_person()

'''
Class Person defines yet another specially named method, __lt__. This
method overloads the < operator. The method Person__lt__ gets called whenever
the first argument to the < operator is of type Person . The __lt__ method in class
Person is implemented using the binary < operator of type str . The expression
self.name < other.name is shorthand for self.name.__lt__(other.name) . Since
self.name is of type str , this __lt__ method is the one associated with type str .

In addition to providing the syntactic convenience of writing infix expres-
sions that use < , this overloading provides automatic access to any polymorphic
method defined using __lt__ . The built-in method sort is one such method. So,
for example, if pList is a list composed of elements of type Person , the call
pList.sort() will sort that list using the __lt__ method defined in class Person .
'''