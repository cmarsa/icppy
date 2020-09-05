# apply_function_to_list.py
'''
In Python, functions are first-class objects. That means that they can be treated
like objects of any other type, e.g., int or list . They have types, e.g., the expres-
sion type(abs) has the value <type 'built-in_function_or_method'> ; they can ap-
pear in expressions, e.g., as the right-hand side of an assignment statement or as
an argument to a function; they can be elements of lists; etc.
Using functions as arguments allows a style of coding called higher-order
programming.
'''
from factorial import factorial_recursive
from fibonacci import fibonacci_recursive

def apply_to_each(L, f):
    '''
    Assumes L is a list, f a function
    Mutates L by replacing each element, e, of L by f(e)
    '''
    for i in range(0, len(L)):
        L[i] = f(L[i])


def test_apply_to_each():
    L = [1, -2, 3.33]
    print('L =', L)
    print('Apply abs to each element of L.')
    apply_to_each(L, abs)
    print('L =', L)
    print('Apply int to each element of', L)
    apply_to_each(L, int)
    print('L =', L)
    print('Apply factorial to each element of', L)
    apply_to_each(L, factorial_recursive)
    print('L =', L)
    print('Apply Fibonnaci to each element of', L)
    apply_to_each(L, fibonacci_recursive)
    print('L =', L)


if __name__ == '__main__':
    test_apply_to_each()

'''
The function applyToEach is called higher-order because it has an argument
that is itself a function.
'''