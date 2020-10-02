# mammal.py
import numpy as np
import matplotlib.pyplot as plt
from KMeans import try_kmeans, dissimilarity
from Example import Example
from metrics import std_dev


def z_scale_features(vals):
    '''
    '''
    result = np.array(vals)
    mean = sum(result) / len(result)
    result = result - mean
    return result / std_dev(result)


def interpolation_scale_features(vals):
    '''
    '''
    min_val, max_val = min(vals), max(vals)
    fit = np.polyfit([min_val, max_val], [0, 1], 1)
    return np.polyval(fit, vals)
    


def read_mammal_data(filename, scale):
    data_file = open(filename, 'r')
    num_features = 0
    # process lines at top of file
    for line in data_file: # find number of features
        if line[0:6] == '#Label':
            break
        if line[0:5] != '#Name':
            num_features += 1
    feature_vals = []
    # procedure feature_vals, species_names, and label_list
    feature_vals, species_names, label_list = [], [], []
    for i in range(num_features):
        feature_vals.append([])
    # continue processing lines in file, starting after comments
    for line in data_file:
        # remove newline, then split
        data_line = line[:-1].split(',')
        species_names.append(data_line[0])
        class_label = data_line[-1]
        label_list.append(class_label)
        for i in range(num_features):
            feature_vals[i].append(float(data_line[i + 1]))
    # use feature_vals to build list containing the feature vectors
    # for each mammal, scaling features as indicated
    for i in range(0, num_features):
        feature_vals[i] = scale(feature_vals[i])  # use the scale function passed as param
    feature_vector_list = []
    for mammal in range(0, len(species_names)):
        feature_vector = []
        for feature in range(num_features):
            feature_vector.append(feature_vals[feature][mammal])
        feature_vector_list.append(feature_vector)
    return feature_vector_list, label_list, species_names


def build_mammal_examples(feature_list, label_list, species_names):
    examples = []
    for i in range(0, len(species_names)):
        features = np.array(feature_list[i])
        example = Example(species_names[i], features, label_list[i])
        examples.append(example)
    return examples


def test_teeth(num_clusters, num_trials, scale = lambda x: x):
    features, labels, species = read_mammal_data('input/mammal_identition.txt', scale)
    examples = build_mammal_examples(features, labels, species)
    best_clustering = try_kmeans(examples, num_clusters, num_trials)
    for c in best_clustering:
        names = ''
        for p in c.members():
            names += p.get_name() + ', '
        print('\n' + names[:-2]) # remove trailing comma and space
        herbivores, carnivores, omnivores = 0, 0, 0
        for p in c.members():
            if p.get_label() == '0':
                herbivores += 1
            elif p.get_label() == '1':
                carnivores += 1
            else:
                omnivores += 1
        print(herbivores, 'herbivores', carnivores, 'carnivores', omnivores, 'omnivores')



if __name__ == '__main__':
    print('================ Clustering with z-scaling ================')
    test_teeth(3, 40, z_scale_features)
    print('================ Clusteting with interpolation-scaling ================')
    test_teeth(3, 40, interpolation_scale_features)