# fibonacci.py

def fibonacci_recursive(n):
    '''
    Assumes n int >= 0
    Returns Fibonacci of n
    '''
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n):
    '''
    Assumes n in >= 0
    Returns Fibonacci of n
    '''
    if n == 0 or n == 1:
        return 1
    else:
        a, b = 0, 1
        for __ in range(0, n):
            c = a + b
            a = b
            b = c
    return c


def test_fibonacci(n):
    for i in range(0, n + 1):
        print(f'F({i}) : ', fibonacci_recursive(i))
        assert fibonacci_iterative(i) == fibonacci_recursive(i)


if __name__ == '__main__':
    test_fibonacci(30)
