# boston_marathon.py
import io
import random
import numpy as np
import matplotlib.pyplot as plt
from simplestats import mean, std_dev


def get_boston_marathon_data(filename):
    '''
    Read the contents of the given file. Assumes the file
        in a commma-separated format, with 6 elements in each entry:
            0. Name (string)
            1. Gender (string)
            2. Age (int)
            3. Division (int)
            4. Country (string)
            5. Overall time (float)
    Returns: dict containing a list for each of the 6 variables
    '''
    data = {}
    f = io.open(filename)
    line = f.readline()
    data['name'], data['gender'], data['age'] = [], [], []
    data['division'], data['country'], data['time'] = [], [], []
    while line != '':
        split = line.split(',')
        data['name'].append(split[0])
        data['gender'].append(split[1])
        data['age'].append(int(split[2]))
        data['division'].append(int(split[3]))
        data['country'].append(split[4])
        data['time'].append(float(split[5][:-1]))
        line = f.readline()
    f.close()
    return data


def plot_histogram(data, bins, title, x_label, y_label):
    plt.hist(data, bins, color = 'gray', edgecolor = 'k')
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    data_mean = mean(data)
    data_std_dev = std_dev(data)
    plt.annotate(f'Mean = {round(data_mean, 2)}\nSD = {round(data_std_dev, 2)}',
                 fontsize = 10, xy = (0.65, 0.75), xycoords = 'axes fraction')
    plt.show()


def sample_times(times, num_examples):
    '''
    Assumes times a lsit of floats representing finishing
    times of all runners. num_examples an int
    Generates a random sample of size num_examples, and produces
    a histogram showing the distribution along with its mean and standard
    deviation.
    '''
    sample = random.sample(times, num_examples)
    plot_histogram(sample, 10, 'Sample of size ' + str(num_examples),
                   'Minutes to Complete Race', 'Number of Runners')


def test_sample_times():
    sample_size = 320
    times = get_boston_marathon_data('input/bm_results_2012.txt')['time']
    sample_times(times, sample_size)


def minutes_to_complete_race():
    times = get_boston_marathon_data('input/bm_results_2012.txt')['time']
    plot_histogram(times, 20, '2012 Boston Marathon',
                   'Minutes to complete the race', 'number of runners')


def plot_mean_estimation_error_bars():
    times = get_boston_marathon_data('input/bm_results_2012.txt')['time']
    mean_of_means, std_of_means = [], []
    sample_sizes = range(50, 2000, 200)
    for sample_size in sample_sizes:
        sample_means = []
        for t in range(20):
            sample = random.sample(times, sample_size)
            sample_means.append(sum(sample)/sample_size)
        mean_of_means.append(mean(sample_means))
        std_of_means.append(std_dev(sample_means))
    plt.errorbar(sample_sizes, mean_of_means,
                 yerr = 1.96 * np.array(std_of_means),
                 label = 'Estimated mean and 95% confidence interval',
                 color = 'k', ecolor = 'k')
    plt.xlim(0, max(sample_sizes) + 50)
    plt.axhline(mean(times), linestyle = '--',
                label = 'Population mean')
    plt.title('Estimates of Mean Finishing Time')
    plt.xlabel('Sample size')
    plt.ylabel('Finishing time (minutes)')
    plt.legend(loc = 'best')
    plt.show()

if __name__ == '__main__':
    # minutes_to_complete_race()
    # test_sample_times()
    plot_mean_estimation_error_bars()