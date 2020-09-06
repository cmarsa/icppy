# knapsack_decision_tree.py
import random
from Item import Item


def max_val(to_consider, available):
    '''
    Assumes to_consider a list of items, avail a weight,
    Returns a tuple of the total value of a solution to the
        0/1 knapsack problem and the items of that solution.
    '''
    if to_consider == [] or available == 0:
        result = (0, ())
    elif to_consider[0].get_weight() > available:
        # explore right branch only
        result = max_val(to_consider[1:], available)
    else:
        next_item = to_consider[0]
        # explore left branch
        with_val, with_to_take = max_val(to_consider[1:],
                                         available - next_item.get_weight())
        with_val += next_item.get_value()
        # explore right branch
        without_val, without_to_take = max_val(to_consider[1:], available)
        # choose better branch
        if with_val > without_val:
            result = (with_val, with_to_take + (next_item,))
        else:
            result = (without_val, without_to_take)
    return result


def fast_max_val(to_consider, available, memo = {}):
    '''
    Assumes to_consider a list of items, available a weight
        memo supplied by recursive calls
    Returns a tuple of the total value of a solution to the
        0/1 knapsack problem and the items of that solution.
    '''
    if (len(to_consider), available) in memo:
        result = memo[(len(to_consider), available)]
    elif to_consider == [] or available == 0:
        result = (0, ())
    elif to_consider[0].get_weight() > available:
        # explore right branch only
        result = fast_max_val(to_consider[1:], available, memo)
    else:
        next_item = to_consider[0]
        # explore left branch
        with_val, with_to_take = \
            fast_max_val(to_consider[1:],
                         available - next_item.get_weight(), memo)
        with_val += next_item.get_value()
        # explore right branch
        without_val, without_to_take = fast_max_val(to_consider[1:],
                                                    available, memo)
        with_val += next_item.get_value()
        # explore right branch
        without_val, without_to_take = fast_max_val(to_consider[1:],
                                                    available, memo)
        # choose better branch
        if with_val > without_val:
            result = (with_val, with_to_take + (next_item,))
        else:
            result = (without_val, without_to_take)
    memo[(len(to_consider), available)] = result
    return result


def small_test():
    print("Small test:")
    names = ['a', 'b', 'c', 'd']
    vals = [6, 7, 8, 9]
    weights = [3, 3, 2, 5]
    items = []
    for i in range(0, len(vals)):
        items.append(Item(names[i], vals[i], weights[i]))
    val, taken = max_val(items, 5)
    for item in taken:
        print(item)
    print('Total value of items taken: ', val, '\n')


def build_many_items(num_items, max_val, max_weight):
    items = []
    for i in range(num_items):
        items.append(Item(str(i),
                          random.randint(1, max_val),
                          random.randint(1, max_weight)))
    return items


def big_test(num_items):
    print("Big test:")
    items = build_many_items(num_items, 10, 10)
    value, taken = fast_max_val(items, 10)
    print('Items Taken')
    for item in taken:
        print(item)
    print('Total value of items taken: ', value, '\n')


if __name__ == '__main__':
    small_test()
    big_test(950)