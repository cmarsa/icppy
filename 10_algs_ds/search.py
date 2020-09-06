# search.py
'''
Some simple implementations of search algorithms
'''

def linear_search(L, e):
    ''''
    Assumes L is a list, the elements of which are in
        ascending order.
    Returns True if e is in L and False otherwise.
    '''
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False


def binary_search_recursive(L, e):
    '''
    Assumes L is a list, the elements of which are in
        ascending order.
    Returns True if e is in L and False otherwise
    '''
    def __recursive_search(L, e, low, high):
        # decrements high - low
        if high == low:
            return L[low] == e
        mid = (low + high) // 2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid:
                return False
            else:
                return __recursive_search(L, e, low, mid - 1)
        else:
            return __recursive_search(L, e, mid + 1, high)
    
    if len(L) == 0:
        return False
    else:
        return __recursive_search(L, e, 0, len(L) - 1)


