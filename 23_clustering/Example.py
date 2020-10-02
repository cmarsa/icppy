# Example.py
from .metrics import minkovski_distance

class Example:
    '''
    Class Example will be used to build the samples to be clustered. Associated with
    each example is a name, a feature vector, and an optional label. The distance
    method returns the Euclidean distance between two examples.
    '''
    def __init__(self, name, features, label = None):
        # assumes features is an array of floats
        self.name = name
        self.features = features
        self.label = label
    
    def dimensionality(self):
        return len(self.features)
    
    def get_features(self):
        return self.features[:]
    
    def get_label(self):
        return self.label
    
    def get_name(self):
        return self.name
    
    def distance(self, other):
        return minkovski_distance(self.get_features(),
                                  other.get_features(), 2)
    
    def __str__(self):
        return self.name + ':' + str(self.features) + ':' \
            + str(self.label)
