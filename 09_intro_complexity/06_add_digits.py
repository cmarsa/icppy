# 06_add_digits.py
from .05_int_to_str import int_to_str

def add_digits(n):
    '''
    Assumes n is a nonnegative int
    Returns the sum of the digits in n
    '''
    string_rep = int_to_str(n)
    val = 0
    for c in string_rep:
        val += int(c)
    return val

'''
The complexity of converting n to a string using intToStr is O(log(n)) , and
intToStr returns a string of length O(log(n)) . The for loop will be executed
O(len(stringRep)) times, i.e., O(log(n)) times. Putting it all together, and assum-
ing that a character representing a digit can be converted to an integer in con-
stant time, the program will run in time proportional to O(log(n)) + O(log(n)) ,
which makes it O(log(n)) .
'''