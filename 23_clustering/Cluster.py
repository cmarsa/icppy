# Cluster.py
'''
Clustering is an optimization problem. The goal is to find a set of clusters
that optimizes an objective function, subject to some set of constraints. Given a
distance metric that can be used to decide how close two examples are to each
other, we need to define an objective function that minimizes the distance be-
tween examples in the same cluster, i.e., minimizes the dissimilarity of the exam-
ples within a cluster.
'''
import numpy as np
from Example import Example


class Cluster:
    '''
    A cluster is a set of examples.
    The two interesting methods in Cluster are compute_centroid and variability.
    Think of the centroid of a cluster as its center of mass. The method
    compute_centroid returns an example with a feature vector equal to the Euclidean
    mean of the feature vectors of the examples in the cluster.
    The method variability provides a measure of the coherence of the cluster.
    '''
    def __init__(self, examples):
        '''
        Assumes examples a non-empty list of Examples
        '''
        self.examples = examples
        self.centroid = self.compute_centroid()
    
    def update(self, examples):
        '''
        Assume examples is a non-empty list of examples
        Replace examples; reurns amount centroid has changed
        '''
        old_centroid = self.centroid
        self.examples = examples
        self.centroid = self.compute_centroid()
        return old_centroid.distance(self.centroid)
    
    def compute_centroid(self):
        vals = np.array([0.0] * self.examples[0].dimensionality())
        for e in self.examples:
            vals += e.get_features()
        centroid = Example('centroid', vals / len(self.examples))
        return centroid
    
    def get_centroid(self):
        return self.centroid
    
    def variability(self):
        total_distance = 0.0
        for e in self.examples:
            total_distance += (e.distance(self.centroid)) ** 2
        return total_distance
    
    def members(self):
        for e in self.examples:
            yield e
    
    def __str__(self):
        names = []
        for e in self.examples:
            names.append(e.get_name())
        names.sort()
        result = 'Cluster with centroid' \
            + str(self.centroid.get_features()) + ' contains:\n'
        for e in names:
            result = result + e + ', '
        return result[:-2]
