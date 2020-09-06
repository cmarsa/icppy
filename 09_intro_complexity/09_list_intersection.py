# 09_list_intersection.py

def intersect(L1, L2):
    '''
    Assumes: L1 and L2 are lists
    Returns a list without duplicates that is the intersection of
    L1 and L2
    '''
    # build a list containing common elements
    tmp = []
    for e1 in L1:
        for e2 in L2:
            if e1 == e2:
                tmp.append(e1)
                break
    # build a list without duplicates
    result = []
    for e in tmp:
        if e not in result:
            result.append(e)
    return result


'''
The running time for the part building the list that might contain duplicates
is clearly O( len(L1) * len(L2)) . At first glance, it appears that the part of the code
that builds the duplicate-free list is linear in the length of tmp , but it is not. The
test e not in result potentially involves looking at each element in result , and is
therefore O(len(result)) ; consequently the second part of the implementation is
O(len(tmp) * len(result)) . However, since the lengths of result and tmp are bound-
ed by the length of the smaller of L1 and L2 , and since we ignore additive terms,
the complexity of intersect is O(len(L1) * len(L2)).
'''