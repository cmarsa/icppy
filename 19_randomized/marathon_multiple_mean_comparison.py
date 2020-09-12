import io
import random
import numpy as np
import matplotlib.pyplot as plt
from simplestats import mean, std_dev
from scipy import stats


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


def compare_mean_finishing_time_countries():
    data = get_boston_marathon_data('input/bm_results_2012.txt')
    countries_to_compare = ['BEL', 'BRA', 'FRA', 'JPN', 'ITA']
    # build mapping from country to list of female finishing times
    country_times = {}
    for i in range(len(data['name'])):
        if data['country'][i] in countries_to_compare and \
                data['gender'][i] == 'F':
            try:
                country_times[data['country'][i]].append(data['time'][i])
            except KeyError:
                country_times[data['country'][i]] = [data['time'][i]]
    
    # compare finishing times of countries
    for c1 in countries_to_compare:
        for c2 in countries_to_compare:
            if c1 < c2:
                p_val = stats.ttest_ind(country_times[c1],
                                        country_times[c2],
                                        equal_var = False)[1]
                if p_val < 0.05:
                    print(c1, 'and', c2,
                          'have significantly different means,',
                          'p-value =', round(p_val, 4))


def check_multiple_hypotheses():
    num_hyps = 20
    sample_size = 30
    population = []
    for i in range(5000):
        population.append(random.gauss(0, 1))
    
    sample_1, sample_2 = [], []
    for i in range(num_hyps):
        sample_1.append(random.sample(population, sample_size))
        sample_2.append(random.sample(population, sample_size))
    # check pairs for statistically significant difference
    num_sig = 0
    for i in range(num_hyps):
        if stats.ttest_ind(sample_1[i], sample_2[i])[1] < 0.05:
            num_sig += 1
    print('Number of statistiaclly significant (p < 0.05) results: ',
          num_sig)

if __name__ == "__main__":
    # compare_mean_finishing_time_countries()
    check_multiple_hypotheses()