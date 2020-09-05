# InfoHiding.py
'''
Some programming languages (Java and C++, for example) provide mecha-
nisms for enforcing information hiding. Programmers can make the attributes of
a class private, so that clients of the class can access the data only through the ob-
ject's methods. Python 3 uses a naming convention to make attributes invisible
outside the class. When the name of an attribute starts with __ but does not end
with __ , that attribute is not visible outside the class.
'''

class InfoHiding:
    def __init__(self):
        self.visible = 'Look at me'
        self.__also_visible__ = 'Look at me too'
        self.__invisible = 'Don\'t look at me directly'
    
    def print_visible(self):
        print(self.visible)
    
    def print_invisible(self):
        print(self.__invisible)
    
    def __print_invisible(self):
        print(self.__invisible)
    
    def __print_invisible__(self):
        print(self.__invisible)


class SubClass(InfoHiding):
    def __init__(self):
        print('from SubClass', self.__invisible)

def test_InfoHiding():
    try:
        test = InfoHiding()
        print(test.visible)
        print(test.__also_visible__)
        print(test.__invisible)
    except AttributeError as e:
        print(e)
    print("")

    try:
        test = InfoHiding()
        test.print_invisible()
        test.__print_invisible__()
        test.__print_invisible()
    except AttributeError as e:
        print(e)
    print("")


def test_SubClass():
    try:
        test = SubClass()
    except AttributeError as e:
        print(e)
    print("")

if __name__ == '__main__':
    test_InfoHiding()
    test_SubClass()