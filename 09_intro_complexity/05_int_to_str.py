# int_to_str.py

def int_to_str(i):
    '''
    Assume i is a nonnegative int
    Returns a decimal string representation of i
    '''
    digits = '0123456789'
    if i == 0:
        return '0'
    result = ''
    while i > 0:
        result = digits[i%10] + result
        i = i // 10
    return result


def test_int_to_str():
    x = 56789
    x_str = int_to_str(x)
    print('x:', x)
    print('x_str:', x_str)


if __name__ == '__main__':
    test_int_to_str()

'''
Since there are no function or method calls in this code, we know that we on-
ly have to look at the loops to determine the complexity class. There is only one
loop, so the only thing that we need to do is characterize the number of itera-
tions. That boils down to the number of times we can use integer division to di-
vide i by 10 before getting a result of 0 .
So, the complexity of in_to_str is O(log(i)) .
'''
