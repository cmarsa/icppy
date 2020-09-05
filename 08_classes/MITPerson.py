# MITPerson.py

from Person import Person

class MITPerson(Person):
    '''
    '''
    next_id = 0

    def __init__(self, name):
        Person.__init__(self, name)
        self.id_num = MITPerson.next_id
        MITPerson.next_id += 1
    
    def get_id(self):
        return self.id_num
    
    def is_student(self):
        return isinstance(self, Student)
    
    def __lt__(self, other):
        return self.id_num < other.id_num


class Student(MITPerson):
    pass


class UG(Student):
    def __init__(self, name, class_year):
        MITPerson.__init__(self, name)
        self.year = class_year
    
    def get_class(self):
        return self.year


class Grad(Student):
    pass


class TransferStudent(Student):
    def __init__(slef, name, from_school):
        MITPerson.__init__(self, name, from_school)
        self.from_school = from_school
    
    def get_old_school(self):
        return self.from_school


def test_MITPerson():
    p1 = MITPerson('Mark Guttag')
    p2 = MITPerson('Billy Bob Beaver')
    p3 = MITPerson('Billy Bob Beaver')
    p4 = Person('Billy Bob Beaver')
    
    print('p1 < p2 =', p1 < p2)
    print('p3 < p2 =', p3 < p2)
    print('p4 < p1 =', p4 < p1)


def test_Grad_UG():
    p5 = Grad('Buzz Aldrin')
    p6 = UG('Billy Beaver', 1984)
    print(p5, 'is a graduate student is', type(p5) == Grad)
    print(p5, 'is an undergraduate student is', type(p5) == UG)


if __name__ == '__main__':
    test_MITPerson()
    print("")

    test_Grad_UG()

'''
The class MITPerson inherits attributes from its parent class, Per-
son , including all of the attributes that Person inherited from its parent class, ob-
ject . In the jargon of object-oriented programming, MITPerson is a subclass of
Person , and therefore inherits the attributes of its superclass. In addition to what
it inherits, the subclass can:
• Add new attributes. For example, the subclass MITPerson has added the class
    variable nextIdNum , the instance variable idNum , and the method getIdNum .
• Override, i.e., replace, attributes of the superclass. For example, MITPerson
    has overridden __init__ and __lt__ . When a method has been overridden, the
    version of the method that is executed is based on the object that is used to in-
    voke the method. If the type of the object is the subclass, the version defined in
    the subclass will be used. If the type of the object is the superclass, the version
    in the superclass will be used.

The method MITPerson.__init__ first invokes Person.__init__ to initialize the
inherited instance variable self.name . It then initializes self.idNum , an instance
variable that instances of MITPerson have but instances of Person do not.
The instance variable self.idNum is initialized using a class variable, nextId-
Num , that belongs to the class MITPerson , rather than to instances of the class.
When an instance of MITPerson is created, a new instance of nextIdNum is not cre-
ated. This allows __init__ to ensure that each instance of MITPerson has a unique
idNum .

in test_MITPerson():
Since p1 , p2 , and p3 are all of type MITPerson , the interpreter will use the __lt__
method defined in class MITPerson when evaluating the first two comparisons, so
the ordering will be based on identification numbers. In the third comparison,
the < operator is applied to operands of different types. Since the first argument
of the expression is used to determine which __lt__ method to invoke, p4 < p1 is
shorthand for p4.__lt__(p1) . Therefore, the interpreter uses the __lt__ method as-
sociated with the type of p4 , Person , and the “people” will be ordered by name.

What happens if we try
Print('p1 < p4 =', p1 < p4)
The runtime system will invoke the __lt__ operator associated with the type of
p1 , i.e., the one defined in class MITPerson . This will lead to the exception
AttributeError: 'Person' object has no attribute 'idNum'
because the object to which p4 is bound does not have an attribute idNum .

By introducing the class Grad , we gain the ability to create two different kinds
of students and use their types to distinguish one kind of object from another.
For example, the code
p5 = Grad('Buzz Aldrin')
p6 = UG('Billy Beaver', 1984)
print(p5, 'is a graduate student is', type(p5) == Grad)
print(p5, 'is an undergraduate student is', type(p5) == UG)


'''

