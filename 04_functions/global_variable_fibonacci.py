# fibonacci_rec_num_calls.py

def fibonacci(n):
    '''
    '''
    global num_fib_calls
    num_fib_calls += 1
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def test_fibonacci(n):
    for i in range(n + 1):
        global num_fib_calls
        num_fib_calls = 0
        print(f'F({i}) : ', fibonacci(i))
        print(f'Fibonacci called', num_fib_calls, 'times...')


if __name__ == '__main__':
    test_fibonacci(10)