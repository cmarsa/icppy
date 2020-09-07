# Drunk.py
import random

class Drunk:
    def __init__(self, name = None):
        '''Assumes name is a str'''
        self.name = name
    
    def __str__(self):
        if self != None:
            return self.name
        return 'Anonymous'


class UsualDrunk(Drunk):
    def take_step(self):
        step_choices = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        return random.choice(step_choices)


class ColdDrunk(Drunk):
    def take_step(self):
        step_choices = [(0, 1), (0, -2), (1, 0), (-1, 0)]
        return random.choice(step_choices)


class EWDrunk(Drunk):
    def take_step(self):
        step_choices = [(1, 0), (-1, 0)]
        return random.choice(step_choices)
