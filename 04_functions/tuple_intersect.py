# tuple_intersect.py

def tuple_intersect(t1, t2):
    '''
    Assumes t1 and t2 are tuples
    Returns a tuple containing elements that are in
        both t1 and t2
    '''
    result = ()
    for element in t1:
        if element in t2:
            result += (element, )
    return result


def test_tuple_intersect():
    t1 = (4, 5, 6, 3, 4, 5, 6, 7, 4, 3)
    t2 = (4, 3, 1, 7, 1, 0)
    intersection = tuple_intersect(t1, t2)
    print('t1: ', t1)
    print('t2: ', t2)
    print('intersection: ', intersection)


if __name__ == '__main__':
    test_tuple_intersect()