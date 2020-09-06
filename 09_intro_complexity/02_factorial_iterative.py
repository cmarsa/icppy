# 02_factorial.py

def factorial(n):
    '''
    Assumes n is a natural number
    Returns n!
    '''
    answer = 1
    while n > 1:
        answer *= n
        n -= 1
    return answer

'''
The number of steps required to run this program is something like 2 ( 1 for
the initial assignment statement and 1 for the return ) + 5n (counting 1 step for
the test in the while , 2 steps for the first assignment statement in the while loop,
and 2 steps for the second assignment statement in the loop). So, for example, if n
is 1000 , the function will execute roughly 5002 steps.
It should be immediately obvious that as n gets large, worrying about the dif-
ference between 5n and 5n+2 is kind of silly. For this reason, we typically ignore
additive constants when reasoning about running time. Multiplicative constants
are more problematical. Should we care whether the computation takes 1000
steps or 5000 steps? Multiplicative factors can be important. Whether a search
engine takes a half second or 2.5 seconds to service a query can be the difference
between whether people use that search engine or go to a competitor.
'''