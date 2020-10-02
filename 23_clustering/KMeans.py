# KMeans.py
'''
K-means clustering is probably the most widely used clustering method. 165 Its
goal is to partition a set of examples into k clusters such that
* Each example is in the cluster whose centroid is the closest centroid to that ex-
ample, and
* The dissimilarity of the set of clusters is minimized.
Unfortunately, finding an optimal solution to this problem on a large data set
is computationally intractable. Fortunately, there is an efficient greedy algo-
rithm 166 that can be used to find a useful approximation. It is described by the
pseudocode
    randomly choose k examples as initial centroids of clusters
    while true:
        1. Create k clusters by assigning each example to closest centroid
        2. Compute k new centroids by averaging the examples in each
        cluster
        3. If none of the centroids differ from the previous iteration:
        return the current set of clusters
'''
import random
from Cluster import Cluster


def dissimilarity(clusters):
    tot_dist = 0.0
    for c in clusters:
        tot_dist += c.variability()
    return tot_dist


def kmeans(examples, k, verbose = False):
    # get k randomly chosen initial centroids, create cluster for each
    initial_centroids = random.sample(examples, k)
    clusters = []
    for e in initial_centroids:
        clusters.append(Cluster([e]))
    # iterate unitil centroids do not change
    converged = False
    num_iterations = 0
    while not converged:
        num_iterations += 1
        # create a list containing k distinct empty lists
        new_clusters = []
        for i in range(k):
            new_clusters.append([])
        # associate each example with closest centroid
        for e in examples:
            # find the centroid closest to e
            smallest_distance = e.distance(clusters[0].get_centroid())
            index = 0
            for i in range(1, k):
                distance = e.distance(clusters[i].get_centroid())
                if distance < smallest_distance:
                    smallest_distance = distance
                    index = i
            # add e to the list of examples for appropriate cluster
            new_clusters[index].append(e)
        # avoid having empty clusters
        for c in new_clusters:
            if len(c) == 0:
                raise ValueError('Empty cluster')
        # update each cluster; check if a centroid has changed
        converged = True
        for i in range(0, k):
            if clusters[i].update(new_clusters[i]) > 0.0:
                converged = False
        if verbose:
            print('Iteration #' + str(num_iterations))
            for c in clusters:
                print(c)
            print('') # add blank line
        return clusters

def try_kmeans(examples, k, num_trials, verbose = False):
    '''
    Calls kmeans num_trials times and returns the result with the
    lowest dissimilarity
    '''
    best = kmeans(examples, k, verbose)
    min_dissimilarity = dissimilarity(best)
    trial = 1
    while trial < num_trials:
        try:
            clusters = kmeans(examples, k, verbose)
        except ValueError:
            continue # if failed, try again
        curr_dissimilarity = dissimilarity(clusters)
        if curr_dissimilarity < min_dissimilarity:
            best = clusters
            min_dissimilarity = curr_dissimilarity
        trial += 1
    return best