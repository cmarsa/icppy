# find_extreme_divisors.py

def find_extreme_divisors(n1, n2):
    '''
    Assumes that n1 and n2 are positive ints
    Returns a tuple containing the smallest common divisor > 1
        and the largest common divisor of n1 and n2. If no common
        divisor, returns (None, None)
    '''
    min_val, max_val = None, None
    for i in range(2, min(n1, n2) + 1):
        if n1 % i == 0 and n2 % i == 0:
            if min_val == None:
                min_val = i
            max_val = i
    return (min_val, max_val)


def test_find_extreme_divisors():
    for n1, n2 in [(20, 50), (4, 16), (100, 200)]:
        min_div, max_div = find_extreme_divisors(n1, n2)
        print(
            f'Extreme divisors of {n1} and {n2} are: min_div: {min_div} and max_div: {max_div}'
        )


if __name__ == '__main__':
    test_find_extreme_divisors()