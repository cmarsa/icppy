# is_prime.py

def is_prime(n):
    '''
    Assumes n is a non-negative int.
    Returns True if n is prime, False otherwise.
    '''
    assert n >= 0, f'n ({n}) is not equal or greater than 0.'
    if n == 0 or n == 1 or n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def test_is_prime():
    for n in range(0, 2000):
        print(f'is {n} prime?: ', is_prime(n))
    
    for n in range(5000, 200000, 3):
        print(f'is {n} prime?: ', is_prime(n))


if __name__ == '__main__':
    test_is_prime()
