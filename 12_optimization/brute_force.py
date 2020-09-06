# brute_force.py
from Item import Item
from Item import build_items
from powerset import gen_powerset

def choose_best(powerset, max_weight, get_val, get_weight):
    best_val = 0.0
    best_set = None
    # iterate over all possible combinations of the items
    for items in powerset:
        items_val = 0.0
        items_weight = 0.0
        # iterate over the items of the combination
        for item in items:
            # compute items value and weight
            items_val += get_val(item)
            items_weight += get_weight(item)
        # if the sum of weight meets the constraint and
        # the solution is the best so far, save best_value and
        # best_set
        if items_weight <= max_weight and items_val > best_val:
            best_val = items_val
            best_set = items
    # return the best combination of items that meets the constraint
    # and maximum value
    return (best_set, best_val)


def test_choose_best(max_weight = 20):
    items = build_items()
    powerset = gen_powerset(items)
    taken, val = choose_best(powerset, max_weight, Item.get_value,
                             Item.get_weight)
    print('Total value of items taken is', val)
    for item in taken:
        print(item)


if __name__ == '__main__':
    test_choose_best()