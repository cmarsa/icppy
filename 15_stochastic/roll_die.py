# roll_die.py
import random

def roll_die():
    '''Returns a random int between 1 and 6'''
    return random.choice([1, 2, 3, 4, 5, 6])


def roll_n(n):
    result = ''
    for i in range(n):
        result = result + str(roll_die())
    print(result)


def test_roll_n():
    roll_n(5)


if __name__ == '__main__':
    test_roll_n()