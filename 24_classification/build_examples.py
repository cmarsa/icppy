# build_examples.py
import io
import random

class Runner:
    def __init__(self, gender, age, time):
        self.feature_vec = (age, time)
        self.label = gender
    
    def feature_dist(self, other):
        dist = 0.0
        for i in range(0, len(self.feature_vec)):
            dist += abs(self.feature_vec[i] - other.feature_vec[i]) ** 2
        return dist ** 0.5
    
    def get_time(self):
        return self.feature_vec[1]
    
    def get_age(self):
        return self.feature_vec[0]
    
    def get_label(self):
        return self.label
    
    def get_features(self):
        return self.feature_vec
    
    def __str__(self):
        return str(self.get_age()) + ', ' + str(self.get_time()) \
            + ', ' + self.label


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


def build_marathon_examples(filename):
    data = get_boston_marathon_data(filename)
    examples = []
    for i in range(len(data['age'])):
        a = Runner(data['gender'][i], data['age'][i],
                   data['time'][i])
        examples.append(a)
    return examples


def divide_80_20(examples):
    sample_indices = random.sample(range(len(examples)), len(examples) // 5)
    training_set, test_set = [], []
    for i in range(0, len(examples)):
        if i in sample_indices:
            test_set.append(examples[i])
        else:
            training_set.append(examples[i])
    return training_set, test_set
