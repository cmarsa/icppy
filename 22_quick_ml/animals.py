# animals.py
import numpy as np
import matplotlib.pyplot as plt

def minkovski_distance(v1, v2, p):
    '''
    Assumes v1 and v2 are equal length arrays of numbers
    Returns Minkowski distance of order p between v1 and v2
    '''
    distance = 0.0
    for i in range(len(v1)):
        distance += abs(v1[i] - v2[i]) ** p
    return distance ** (1 / p)



class Animal:
    def __init__(self, name, features):
        '''
        Assumes name a string; features a list of numbers
        '''
        self.name = name
        self.features = np.array(features)
    
    def get_name(self):
        return self.name
    
    def get_features(self):
        return self.features
    
    def distance(self, other):
        '''
        Assumes other an Animal instance
        Returns the Euclidean distance betweeen feature vectors
            of self and other.
        '''
        return minkovski_distance(self.get_features(),
                                  other.get_features(), 2)


def compare_animals(animals, precision):
    '''
    ASsumes animals is a list of animals, precision an int >= 0
    Buils a table of Euclidean distance between each anumal
    '''
    # get labels for columns and rows
    column_labels = []
    for a in animals:
        column_labels.append(a.get_name())
    row_labels = column_labels[:]
    table_vals = []
    # get distances between pairs of animals
    # for each row
    for a1 in animals:
        row = []
        # for each column
        for a2 in animals:
            if a1 == a2:
                row.append('--')
            else:
                distance = a1.distance(a2)
                row.append(str(round(distance, precision)))
        table_vals.append(row)
    # produce table
    table = plt.table(rowLabels = row_labels,
                      colLabels = column_labels,
                      cellText = table_vals,
                      cellLoc = 'center',
                      loc = 'center',
                      colWidths = [0.2] * len(animals))
    table.scale(1, 2.5)
    plt.show()


def test_compare_animals():
    rattlesnake = Animal('rattlesnake', [1, 1, 1, 1, 0])
    boa = Animal('boa\nconstrictor', [0, 1, 0, 1, 0])
    dartFrog = Animal('dart frog', [1, 0, 1, 0, 1])
    alligator = Animal('alligator', [1, 1, 0, 1, 1])
    animals = [rattlesnake, boa, dartFrog, alligator]
    compare_animals(animals, 3)

if __name__ == '__main__':
    test_compare_animals()
