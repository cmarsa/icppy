# KNearestNeighbors.py
import random
import matplotlib.pyplot as plt
from build_examples import build_marathon_examples, divide_80_20
from classifier_evaluation import get_stats, accuracy

def find_k_nearest(example, example_set, k):
    k_nearest, distances = [], []
    # build lists containing first k examples and their distances
    for i in range(0, k):
        k_nearest.append(example_set[i])
        distances.append(example.feature_dist(example_set[i]))
    max_dist = max(distances)  # get maximum distance
    # look at examples not yet considered
    for e in example_set[k:]:
        dist = example.feature_dist(e)
        if dist < max_dist:
            # replace farther negihtbot by this one
            max_index = distances.index(max_dist)
            k_nearest[max_index] = e
            distances[max_index] = dist
            max_dist = max(distances)
    return k_nearest, distances


def KNNClassifier(training, test_set, label, k):
    '''
    Assumes training and test_set lists of examples, k an int
    Uses a k-nearest neightbor classifier to predict whether each
        example in test_set has the given label
    Returns numbe rof true positives, false positives,
        true negatives, and false negatives
    '''
    true_pos, false_pos, true_neg, false_neg = 0, 0, 0, 0
    for e in test_set:
        print(true_pos, true_neg, false_pos, false_neg, end = '\r')
        nearest, distances = find_k_nearest(e, training, k)
        # conduct vote
        num_match = 0
        for i in range(len(nearest)):
            if nearest[i].get_label() == label:
                num_match += 1
        if num_match > k // 2:  # guess label
            if e.get_label() == label:
                true_pos += 1
            else:
                false_pos += 1
        else:
            if e.get_label() != label:
                true_neg += 1
            else:
                false_neg += 1
    return true_pos, false_pos, true_neg, false_neg


def PrevalenceClassify(training, test_set, label):
    '''
    Assumes training and test_set lists of examples
    Uses a prevalnece-based classifier to predict
        whether each example in test_set is of class label
    Returns numbe rof true positives, false positives,
        true negatives and false false negatives
    '''
    num_with_label = 0
    for e in training:
        if e.get_label() == label:
            num_with_label += 1
    prob_label = num_with_label / len(training)
    true_pos, false_pos, true_neg, false_neg = 0, 0, 0, 0
    for e in test_set:
        if random.random() < prob_label:  # guess label
            if e.get_label() == label:
                true_pos += 1
            else:
                false_pos += 1
        else:  # guess not label
            if e.get_label() != label:
                true_neg += 1
            else:
                false_neg += 1
    return true_pos, false_pos, true_neg, false_neg


def find_k(training, min_k, max_k, num_folds, label):
    # find average accuracy for range of odd values of k
    accuracies = []
    for k in range(min_k, max_k + 1, 2):
        score = 0.0
        for i in range(num_folds):
            # downsample to reduce computation time
            fold = random.sample(training, min(5000, len(training)))
            examples, test_set = divide_80_20(fold)
            true_pos, false_pos, true_neg, false_neg = \
                KNNClassifier(examples, test_set, label, k)
            score += accuracy(true_pos, false_pos, true_neg, false_neg)
        accuracies.append(score / num_folds)
    plt.plot(range(min_k, max_k + 1, 2), accuracies)
    plt.title('Average Accuracy vs k (' + str(num_folds) + ' folds')
    plt.xlabel('k')
    plt.ylabel('Accuracy')
    plt.show()


def test_knn():
    examples = build_marathon_examples('input/bm_results_2012.txt')
    training, test_set = divide_80_20(examples)
    true_pos, false_pos, true_neg, false_neg = KNNClassifier(training, test_set, 'M', 9)
    get_stats(true_pos, false_pos, true_neg, false_neg)


def test_knn_downsample():
    examples = build_marathon_examples('input/bm_results_2012.txt')
    training, test_set = divide_80_20(examples)
    reduced_training = random.sample(training, len(training) // 10)
    true_pos, false_pos, true_neg, false_neg = \
        KNNClassifier(reduced_training, test_set, 'M', 9)
    get_stats(true_pos, false_pos, true_neg, false_neg)


def test_find_k():
    examples = build_marathon_examples('input/bm_results_2012.txt')
    training, test_set = divide_80_20(examples)
    reduced_training = random.sample(training, len(training) // 10)
    find_k(reduced_training, 1, 21, 1, 'M')


if __name__ == '__main__':
    # test_knn()
    # test_knn_downsample()
    test_find_k()