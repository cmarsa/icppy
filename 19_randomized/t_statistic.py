# t_statistic.py
import scipy
import numpy as np
import matplotlib.pyplot as plt

def visualize_t_statistic():
    t_stat = -2.13165598142
    t_distibution = []
    num_bins = 1000
    for i in range(0, 10000000):
        t_distibution.append(scipy.random.standard_t(198))
    
    plt.hist(t_distibution, bins = num_bins,
             weights = np.array(len(t_distibution) * [1.0]) / len(t_distibution))
    plt.axvline(t_stat, color = 'w')
    plt.axvline(-t_stat, color = 'w')
    plt.title('T-Distribution with 198 Degrees of Freedom')
    plt.xlabel('T-statistic')
    plt.ylabel('Probability')
    plt.show()


if __name__ == '__main__':
    visualize_t_statistic()
