# test_kemans.py
import random
import matplotlib.pyplot as plt
from KMeans import try_kmeans, dissimilarity
from Example import Example


def gen_distribution(x_mean, x_sd, y_mean, y_sd, n, name_prefix):
    samples = []
    for s in range(n):
        x = random.gauss(x_mean, x_sd)
        y = random.gauss(y_mean, y_sd)
        samples.append(Example(name_prefix + str(s), [x, y]))
    return samples


def plot_samples(samples, marker):
    x_vals, y_vals = [], []
    for s in samples:
        x = s.get_features()[0]
        y = s.get_features()[1]
        plt.annotate(s.get_name(), xy = (x, y),
                     xytext = (x + 0.13, y - 0.07),
                     fontsize = 'x-large')
        x_vals.append(x)
        y_vals.append(y)
    plt.plot(x_vals, y_vals, marker)


def contrived_test(num_trials, k, verbose = False):
    x_mean = 3
    x_sd = 1
    y_mean = 5
    y_sd = 1
    n = 10
    d1_samples = gen_distribution(x_mean, x_sd, y_mean, y_sd, n, 'A')
    plot_samples(d1_samples, 'k^')
    d2_samples = gen_distribution(x_mean + 3, x_sd, y_mean + 1, y_sd, n, 'B')
    plot_samples(d2_samples, 'ko')
    clusters = try_kmeans(d1_samples + d2_samples, k, num_trials, verbose)
    print('Final result')
    for c in clusters:
        print('', c)
    plt.show()


def contrived_test_2(num_trials, k, verbose = False):
    x_mean = 3
    x_sd = 1
    y_mean = 5
    y_sd = 1
    n = 8
    d1_samples = gen_distribution(x_mean, x_sd, y_mean, y_sd, n, 'A')
    plot_samples(d1_samples, 'k^')
    d2_samples = gen_distribution(x_mean + 3, x_sd, y_mean, y_sd, n, 'B')
    plot_samples(d2_samples, 'ko')
    d3_samples = gen_distribution(x_mean, x_sd, y_mean + 3, y_sd, n, 'C')
    plot_samples(d3_samples, 'kx')
    clusters = try_kmeans(d1_samples + d2_samples + d3_samples,
                          k, num_trials, verbose)
    plt.ylim(0, 11)
    print('Final result has dissimilarity', round(dissimilarity(clusters), 3))
    for c in clusters:
        print('', c)
    plt.show()


if __name__ == "__main__":
    # contrived_test(50, 2, True)
    contrived_test_2(40, 3)