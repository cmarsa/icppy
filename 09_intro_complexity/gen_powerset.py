# gen_power_set.py
from binary_representation import get_binary_representation


def gen_powerset(L):
    '''
    Assumes L is a list
    Returns a list of lists that contains all possible
    combinations of the elements of L (the power set).
    '''
    powerset = []
    for i in range(0, 2**len(L)):
        bin_str = get_binary_representation(i, len(L))
        subset = []
        for j in range(0, len(L)):
            if bin_str[j] == '1':
                subset.append(L[j])
        powerset.append(subset)
    return powerset

def test_gen_powerset():
    l = ['q', 'r', 't', 'b', 'f', 'g']
    l_power = gen_powerset(l)
    print('l: ', l)
    print('P(l): ', l_power)
    assert len(l_power) == 2 ** len(l)


if __name__ == '__main__':
    test_gen_powerset()


'''
The algorithm is a bit subtle. Consider a list of n elements. We can represent
any combination of elements by a string of n 0’s and 1’s , where a 1 represents the
presence of an element and a 0 its absence. The combination containing no items
is represented by a string of all 0’s , the combination containing all of the items is
represented by a string of all 1’s , the combination containing only the first and
last elements is represented by 100...001 , etc.

* Generate all n-bit binary numbers. These are the numbers from 0 to 2 n .
* For each of these 2 n +1 binary numbers, b , generate a list by selecting those
    elements of L that have an index corresponding to a 1 in b . For example, if L is
    ['x', 'y'] and b is 01 , generate the list ['y'] .

Try running genPowerset on a list containing the first ten letters of the alpha-
bet. It will finish quite quickly and produce a list with 1024 elements. Next, try
running genPowerset on the first twenty letters of the alphabet. It will take more
than a bit of time to run, and return a list with about a million elements. If you
try running genPowerset on all twenty-six letters, you will probably get tired of
waiting for it to complete, unless your computer runs out of memory trying to
build a list with tens of millions of elements. Don’t even think about trying to run
genPowerset on a list containing all uppercase and lowercase letters. Step 1 of the
algorithm generates O(2 len(L) ) binary numbers, so the algorithm is exponential in
len(L ) .
Does this mean that we cannot use computation to tackle exponentially hard
problems? Absolutely not. It means that we have to find algorithms that provide
approximate solutions to these problems or that find perfect solutions on some
instances of the problem. But that is a subject for later chapters.

'''