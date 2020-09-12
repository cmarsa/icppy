# simplestats.py

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
