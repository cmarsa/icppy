# greedy.py

def greedy(items, max_weight, key_function):
    '''
    Assumes Items a list, max_weight >= 0,
        key_function maps elements of Items to numbers
    '''
    # sort the items by the key or criteria to choose from
    items_copy = sorted(items, key = key_function, reverse = True)
    result = []
    total_value, total_weight = 0.0, 0.0
    # iterate over all sorted items
    for i in range(0, len(items_copy)):
        # add the items from best criteria value to lowest
        # if they meet the weight constraint
        if (total_weight + items_copy[i].get_weight()) <= max_weight:
            result.append(items_copy[i])
            total_weight += items_copy[i].get_weight()
            total_value += items_copy[i].get_value()
    # return best greedy solution of item combinations
    return (result, total_value)


def test_greedy(items, max_weight, key_function):
    taken, val = greedy(items, max_weight, key_function)
    print('Total value of items taken is', val)
    for item in taken:
        print('  ', item)


def test_greedys(max_weight = 20):
    items = build_items()
    print('Use greedy by value to fill knapsack of size', max_weight)
    test_greedy(items, max_weight, value)
    print('\nUse greedy by weight to fill knapsack of size', max_weight)
    test_greedy(items, max_weight, weight_inverse)
    print('\nUse greedy by density to fill knapsack of size', max_weight)
    test_greedy(items, max_weight, density)


if __name__ == '__main__':
    test_greedys()