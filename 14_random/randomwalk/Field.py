# Field.py
import random
from .Location import Location

class Field:
    def __init__(self):
        self.drunks = {}
    
    def add_drunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc
    
    def move_drunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        x_dist, y_dist = drunk.take_step()
        current_location = self.drunks[drunk]
        # use move method of Location to get new location
        self.drunks[drunk] = current_location.move(x_dist, y_dist)
    
    def get_loc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]


class OddField(Field):
    def __init__(self, num_holes, x_range, y_range):
        Field.__init__(self)
        self.worm_holes = {}
        for w in range(0, num_holes):
            x = random.randint(-x_range, x_range)
            y = random.randint(-y_range, y_range)
            x_new = random.randint(-x_range, x_range)
            y_new = random.randint(-y_range, y_range)
            new_loc = Location(x_new, y_new)
            self.worm_holes[(x, y)] = new_loc
    
    def move_drunk(self, drunk):
        Field.move_drunk(self, drunk)
        x = self.drunks[drunk].get_x()
        y = self.drunks[drunk].get_y()
        if (x, y) in self.worm_holes:
            self.drunks[drunk] = self.worm_holes[(x, y)]
            