# fast_fibonacci.py

def fast_fibonacci(n, memo = {}):
    '''
    Assumes n is an int >= 0, memo used only by recursive calls
    Returns Fibonacci of n
    '''
    if n == 0 or n == 1:
        return 1
    if memo.get(n):
        return memo[n]
    else:
        memo[n] = fast_fibonacci(n - 1, memo) + fast_fibonacci(n - 2, memo)
        return memo[n]


def test_fast_fibonacci():
    print(fast_fibonacci(11))


if __name__ == '__main__':
    test_fast_fibonacci()