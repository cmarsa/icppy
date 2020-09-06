# sorting.py
'''
We have just seen that if we happen to know that a list is sorted, we can exploit
that information to greatly reduce the time needed to search a list. Does this
mean that when asked to search a list one should first sort it and then perform
the search?
Let O(sortComplexity(L)) be the complexity of sorting a list. Since we know
that we can always search a list in O(len(L)) time, the question of whether we
should first sort and then search boils down to the question, is sortComplexity(L)
+ log(len(L)) less than len(L) ? The answer, sadly, is no. One cannot sort a list
without looking at each element in the list at least once, so it is not possible to
sort a list in sub-linear time.
'''

def selection_sort(L):
    '''
    Assumes that L is a list of elements that can be
        compared using >.
    Sorts L in ascending order
    '''
    suffix_start = 0
    while suffix_start != len(L):
        # look at each element in suffix
        for i in range(suffix_start, len(L)):
            if L[i] < L[suffix_start]:
                # swap position of elements
                L[suffix_start], L[i] = L[i], L[suffix_start]
        suffix_start += 1
    

def merge_sort(L, compare = lambda x, y: x < y):
    '''
    Assumes L is a list, compare defined an ordering
        on elements of L.
    Returns a new sorted list with the same elements as L
    '''
    def __merge(left, right, compare):
        '''
        Assumes left and right are sorted lists and compare
            defines an ordering on the elements.
        Returns a new sorted (by compare) list containing the
            same elements as (left + right) would contain.
        '''
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if compare(left[i], right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        while (i < len(left)):
            result.append(left[i])
            i += 1
        while (j < len(right)):
            result.append(right[j])
            j += 1
        return result
    
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle], compare)
        right = merge_sort(L[middle:], compare)
        return __merge(left, right, compare)
