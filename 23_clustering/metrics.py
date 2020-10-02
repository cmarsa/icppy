# metrics.py

def minkovski_distance(v1, v2, p):
    '''
    Assumes v1 and v2 are equal length arrays of numbers
    Returns Minkowski distance of order p between v1 and v2
    '''
    distance = 0.0
    for i in range(len(v1)):
        distance += abs(v1[i] - v2[i]) ** p
    return distance ** (1 / p)

def mean(X):
    '''
    Assumes that X is a list of numbers
    Returns the mean of X
    '''
    return sum(X) / len(X)


def variance(X):
    '''
    Assumes that X is a list of numbers
    Returns the variance of X
    '''
    mu = mean(X)
    total = 0.0
    for x in X:
        total += (x - mu) ** 2
    return total / len(X)


def std_dev(X):
    '''
    Assumes that X is a list of numbers
    Returns the standard deviation of X
    '''
    return variance(X) ** 0.5


def cv(X):
    '''
    Assumes that X is a list of numbers
    Returns the coefficient of variation of X
    '''
    mu = mean(X)
    try:
        return std_dev(X) / mu
    except ZeroDivisionError:
        return float('nan')

