# Item.py

class Item:
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.weight = w
    
    def get_name(self):
        return self.name
    
    def get_value(self):
        return self.value
    
    def get_weight(self):
        return self.weight
    
    def __str__(self):
        result = '<' + self.name + ', ' + str(self.value) \
            + ', ' + str(self.weight) + '>'
        return result


def value(item):
    return item.get_value()


def weight_inverse(item):
    return 1.0 / item.get_weight()


def density(item):
    return item.get_value() / item.get_weight()


def build_items():
    names = ['clock', 'painting', 'radio', 'vase', 'book', 'computer']
    values = [175, 90, 20, 50, 10, 200]
    weights = [10, 9, 4, 2, 1, 20]
    Items = []
    for i in range(0, len(values)):
        Items.append(Item(names[i], values[i], weights[i]))
    return Items
