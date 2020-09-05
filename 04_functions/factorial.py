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
    assert n > 0
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
    assert n > 0
    if n == 1:
        return n
    else:
        return n * factorial_recursive(n - 1)


def test_factorial():
    for n in range(1, 20):
        iterative, recursive = factorial_iterative(n), factorial_recursive(n)
        assert iterative == recursive
        print(f'{n}! : {iterative}')


if __name__ == '__main__':
    test_factorial()