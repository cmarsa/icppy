# circle.py
'''
A module is a .py file containing Python definitions and statements.
'''
pi = 3.14159

def area(radius):
    return pi * (radius ** 2)


def circumference(radius):
    return 2 * pi * radius


def sphere_surfaces(radius):
    return 4.0 * area(radius)


def sphere_volume(radius):
    return (4.0 / 3.0) * pi * (radius ** 3)
