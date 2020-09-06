# 03_square_root_exhaustive.py
'''
On the other hand, when one is comparing two different algorithms, it is of-
ten the case that even multiplicative constants are irrelevant. Recall that in Chap-
ter 3 we looked at two algorithms, exhaustive enumeration and bisection search,
for finding an approximation to the square root of a floating point number.
'''

def square_root_exhaustive(x, epsilon):
    '''
    Assumes x and epsilon are positive floats & epsilon < 1
    Returns a y such that y*y is whithin epsilon of x
    '''
    step = epsilon ** 2
    answer = 0.0
    while abs(answer ** 2 - x) >= epsilon and answer * answer <= x:
        answer += step
    if answer * answer > x:
        raise ValueError
    return answer


def square_root_bisection(x, epsilon):
    '''
    Assumes x and epsilon are positive floats & epsilon < 1
    Returns a y such that y*y is whithin epsilon of x
    '''
    low = 0.0
    high = max(1.0, x)
    answer = (high + low) / 2.0
    while abs(answer ** 2 - x) >= epsilon:
        if ans ** 2 < x:
            low = answer
        else:
            high = answer
        answer = (high + low) / 2.0
    return answer

'''
We saw that exhaustive enumeration was so slow as to be impractical for
many combinations of x and epsilon . For example, evaluating
square_root_exhaustive(100, 0.0001) requires roughly one billion iterations ofthe while loop.
In contrast, evaluating quare_root_bisection(100, 0.0001) takes roughly twenty iterations of
a slightly more complex while loop. When the difference in the number of itera-
tions is this large, it doesn’t really matter how many instructions are in the loop.
I.e., the multiplicative constants are irrelevant.
'''