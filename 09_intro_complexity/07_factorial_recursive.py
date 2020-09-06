# 07_factorial_recursive.py

def factorial_recursive(n):
    '''
    Assumes that n is a positive integer
    Returns n!
    '''
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

'''
There are no loops in this code, so in order to analyze the complexity we
need to figure out how many recursive calls get made. The series of calls is simply
factorial(x) , factorial(x-1) , factorial(x-2), ... , factorial(1)
The length of this series, and thus the complexity of the function, is O(x) .

Thus far in this chapter we have looked only at the time complexity of our
code. This is fine for algorithms that use a constant amount of space, but this im-
plementation of factorial does not have that property. As we discussed in Chap-
ter 4, each recursive call of factorial causes a new stack frame to be allocated,
and that frame continues to occupy memory until the call returns. At the maxi-
mum depth of recursion, this code will have allocated x stack frames, so the space
complexity is also O(x) .

The impact of space complexity is harder to appreciate than the impact of
time complexity. Whether a program takes one minute or two minutes to com-
plete is quite visible to its user, but whether it uses one megabyte or two mega-
bytes of memory is largely invisible to users. This is why people typically give
more attention to time complexity than to space complexity. The exception oc-
curs when a program needs more space than is available in the fast memory of
the machine on which it is run.

'''