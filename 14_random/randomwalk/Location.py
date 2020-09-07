# Location.py

class Location:
    def __init__(self, x, y):
        '''x and y are numbers'''
        self.x, self.y = x, y
    
    def move(self, delta_x, delta_y):
        '''delta_x and delta_y are numbers'''
        return Location(self.x + delta_x, self.y + delta_y)
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def dist_from(self, other):
        o_x, o_y = other.get_x(), other.get_y()
        x_dist, y_dist = self.x - o_x, self.y - o_y
        return (x_dist ** 2 + y_dist ** 2) ** 0.5
    
    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'
