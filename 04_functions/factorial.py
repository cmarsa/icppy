# factorial.py
'''
In general, a recursive definition is made up of two parts. There is at least
one base case that directly specifies the result for a special case (case 1 in the ex-
ample above), and there is at least one recursive (inductive) case (cases 2 and 3 in
the example above) that defines the answer in terms of the answer to the question
on some other input, typically a simpler version of the same problem.
'''

def factorial_iterative(n):
    '''
    Assumes n an int > 0
    Returns n!
    '''
    result = 1
    while n > 1:
        result = result * n
        n -= 1
    return result


def factorial_recursive(n):
    '''
    Assumes n an int > 0
    Returns n!
    '''
    if n == 1:
        return n
    else:
        return n * factorial_recursive(n - 1)
