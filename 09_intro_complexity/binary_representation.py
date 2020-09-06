# binary_representation.py

def get_binary_representation(n, num_digits = 32):
    '''
    Assumes n and num_digits are non-negative ints
    Returns a str of length num_digits that is a binary
    represnetation of n.
    '''
    result = ''
    while n > 0:
        result = str(n % 2) + result
        n = n // 2
    if len(result) > num_digits:
        raise ValueError('not enough digits')
    for i in range(num_digits - len(result)):
        result = '0' + result
    return result


def test_get_binary_representation():
    n = 2
    print(f'{n:8}', get_binary_representation(n))

    n = 17
    print(f'{n:8}', get_binary_representation(n))

    n = 4876856
    print(f'{n:8}', get_binary_representation(n))


if __name__ == '__main__':
    test_get_binary_representation()