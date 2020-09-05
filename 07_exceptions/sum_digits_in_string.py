# sum_digits_in_string.py
'''
Implement a function that meets the specification below. Use a
try-except block.
def sumDigits(s):
    Assumes s is a string
    Returns the sum of the decimal digits in s
    For example, if s is 'a2b3c' it returns 5
'''

def sum_digits(s):
    number_string = ''
    sum = 0
    for char in s:
        if char.isnumeric():
            number_string += char
        else:
            if number_string != '':
                sum += int(number_string)
                number_string = ''
    return sum


def sum_digits_try_except(s):
    '''
    This function has `the spirit` of the specificacion, but
    does not considers that there may be more than one digit
    decimal numbers and considers each digit independently.
    '''
    number_string = ''
    sum = 0
    for char in s:
        try:
            sum += int(char)
        except ValueError:
            pass
    return sum
            

def test_sum_digits():
    s = 'a2b3c' 
    print(f'Sum of {s} is', sum_digits(s))

    s = 'a2b23c' 
    print(f'Sum of {s} is', sum_digits(s))


def test_sum_digits_try_except():
    s = 'a2b3c' 
    print(f'Sum of {s} is', sum_digits_try_except(s))

    s = 'a2b23c' 
    print(f'Sum of {s} is', sum_digits_try_except(s))

if __name__ == '__main__':
    test_sum_digits()

    test_sum_digits_try_except()