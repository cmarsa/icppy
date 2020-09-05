# mutating_iterating_list.py

def remove_dups_mutation(L1, L2):
    '''
    Assumes that L1 and L2 are lists.
    Removes any element form L1 that also occurs in L2
    '''
    for e1 in L1:
        if e1 in L2:
            L1.remove(e1)


def remove_dups_copy(L1, L2):
    '''
    Assumes that L1 and L2 are lists.
    Removes any element form L1 that also occurs in L2
    '''
    for e1 in L1[:]:
        if e1 in L2:
            L1.remove(e1)

def test_remove_dups_mutation():
    L1 = [1, 2, 3, 4]
    L2 = [1, 2, 5, 6]
    remove_dups_mutation(L1, L2)
    print('L1 = ', L1)


def test_remove_dups_copy():
    L1 = [1, 2, 3, 4]
    L2 = [1, 2, 5, 6]
    remove_dups_copy(L1, L2)
    print('L1 = ', L1)


if __name__ == '__main__':
    print('testing `remove_dups_mutation`')
    test_remove_dups_mutation()
    print('')

    print('tesitng `remove_dups_copy`')
    test_remove_dups_copy()


'''
During a for loop, the implementation of Python keeps track of where it is in
the list using an internal counter that is incremented at the end of each iteration.
When the value of the counter reaches the current length of the list, the loop
terminates. This works as one might expect if the list is not mutated within the
loop, but can have surprising consequences if the list is mutated. In this case, the
hidden counter starts out at 0 , discovers that L1[0] is in L2 , and removes it—
reducing the length of L1 to 3 . The counter is then incremented to 1 , and the code
proceeds to check if the value of L1[1] is in L2 . Notice that this is not the original
value of L1[1] (i.e., 2 ), but rather the current value of L1[1] (i.e., 3 ). As you can
see, it is possible to figure out what happens when the list is modified within the
loop. However, it is not easy. And what happens is likely to be unintentional, as
in this example.

Slicing is not the only way to clone lists in Python. The expression list(L) re-
turns a copy of the list L . If the list to be copied contains mutable objects that you
want to copy as well, import the standard library module `copy` and use the
function `copy.deepcopy` .
'''
