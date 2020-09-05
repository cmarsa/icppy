# IntSet.py

class IntSet:
    '''
    An intSet i a set of integers.
    '''
    # information about the implementation (not the abstraction)
    # value of the set is represented by a list of ints, self.vals.
    # each int the set occurs in self.vals exactly once
    
    def __init__(self):
        '''Create an empry set of integers'''
        self.vals = []
    
    def insert(self, e):
        '''Assumes e is an integer and isnerts e into self'''
        if e not in self.vals:
            self.vals.append(e)
    
    def is_member(self, e):
        '''
        Assumes e is an integer
        Returns True if e is in self, and False otherwise.
        '''
        return e in self.vals
    
    def remove(self, e):
        '''
        Assumes e is an integer and removes e from self
        Raises ValueError if e is not in self
        '''
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')
    
    def get_members(self):
        '''
        Returns a list containing the elements of self.
        Nothing can be assumed about the order of the elements.
        '''
        return self.vals[:]
    
    def __str__(self):
        '''
        Returns a string representation of self
        '''
        self.vals.sort()
        result = ''
        for i in self.vals:
            result = result + str(e) + ','
        return '{' + result[:-1] + '}'   # -1 ommits trailing comma

'''
When a function definition occurs within a class definition, the defined
function is called a method and is associated with the class. These methods are
sometimes referred to as method attributes of the class.


Classes support two kinds of operations:
* Instantiation is used to create instances of the class. For example, the state-
ment s = IntSet() creates a new object of type IntSet . This object is called an
instance of IntSet .
* Attribute references use dot notation to access attributes associated with the
class. For example, s.member refers to the method member associated with the in-
stance s of type IntSet .

As we will see, Python has a number of special method names that start and
end with two underscores. The first of these we will look at is __init__. Whenev-
er a class is instantiated, a call is made to the __init__ method defined in that
class.

When data attributes are associated with a class we call them class variables.
When they are associated with an instance we call them instance variables.

The representation invariant defines which values of the data attributes cor-
respond to valid representations of class instances. The representation invariant
for IntSet is that vals contains no duplicates. The implementation of __init__ is
responsible for establishing the invariant (which holds on the empty list), and the
other methods are responsible for maintaining that invariant. That is why insert
appends e only if it is not already in self.vals .

The last method defined in the class, __str__ , is another one of those special
__ methods. When the print command is used, the __str__ function associated
with the object to be printed is automatically invoked.

All instances of user-defined classes are hashable, and therefore can be used
as dictionary keys. If no __hash__ method is provided, the hash value of the ob-
ject is derived from the function id.

If no __eq__ method is provided, all objects are considered unequal (except to themselves).
If a user-defined __hash__ is provided, it should ensure that the hash value of an object is constant
throughout the lifetime of that object.
'''