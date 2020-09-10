# mean_estimation_variance.py
import random
import matplotlib.pyplot as plt
from scipy import integrate
from simplestats import mean

pi = 3.141592
e = 2.71828

def gaussian(x, mu, sigma):
    f = (1.0 / (sigma * ((2 * pi) ** 0.5)))
    g = e ** -(((x - mu)**2) / (2 * sigma ** 2))
    return f * g


def mean_estimation_normal_dist():
    area = round(integrate.quad(gaussian, -3, 3, (0, 1))[0], 4)
    print('Probability of being withing 3',
        'of true mean of tight dist. = ', area)

    area = round(integrate.quad(gaussian, -3, 3, (0, 100))[0], 4)
    print('Probability of being withing 3',
        'of true mean of tight dist. = ', area)


def test_samples(num_trials, sample_size):
    tight_means, wide_means = [], []
    for t in range(num_trials):
        sample_tight, sample_wide = [], []
        for i in range(sample_size):
            sample_tight.append(random.gauss(0, 1))
            sample_wide.append(random.gauss(0, 100))
        tight_means.append(mean(sample_tight))
        wide_means.append(mean(sample_wide))
    return tight_means, wide_means


def plot_test_samples(log_y = False):
    tight_means, wide_means = test_samples(1000, 40)
    plt.plot(wide_means, 'k^', label = ' SD = 100')
    plt.plot(tight_means, '.', color = 'gray', label = ' SD = 1')
    if log_y:
        plt.semilogy()
    plt.xlabel('Sample Number')
    plt.ylabel('Sample Mean')
    plt.title('Means of Samples of Size ' + str(40))
    plt.legend()

    plt.figure()
    plt.hist(wide_means, bins = 20, label = ' SD = 100',
             color = 'gray', edgecolor = 'k')
    plt.title('Distribution of Sample Means')
    plt.xlabel('Sample Mean')
    plt.ylabel('Frequency of Occurremce')
    plt.legend()
    plt.show()



if __name__ == '__main__':
    # mean_estimation_normal_dist()
    plot_test_samples(log_y = False)