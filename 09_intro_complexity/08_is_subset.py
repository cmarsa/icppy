# 08_is_subset.py

def is_subset(L1, L2):
    '''
    Assumes L1 and L2 are lists.
    Returns True if each element in L1 is also in L2
    and False otherwise
    '''
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True

'''
Each time the inner loop is reached it is executed O(len(L2) times. The func-
tion isSubset will execute the outer loop O(len(L1)) times, so the inner loop will
be reached O(len(L1)) times. Therefore, the complexity of the function isSubset
is O(len(L1) * len(L2)) .
'''