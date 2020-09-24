# bayes.py
import random
from copy import copy


def calculate_bayes(prior_A, prob_B_if_A, prob_B):
    '''
    prior_A: initial estimate of probability of A independent of B
    prior_B_if_A: est. of probability of B assuming A is true
    returns probability of A given B
    '''
    return prior_A * prob_B_if_A / prob_B


def test_calculate_bayes():
    prior_A = 1. / 3
    prob_6_if_A = 1. / 5
    prob6 = (1.0 / 5 + 1.0 / 6 + 1.0 / 7) / 3

    post_A = calculate_bayes(prior_A, prob_6_if_A, prob6)
    print('Probability of type A = ', round(post_A, 4))
    post_A = calculate_bayes(post_A, prob_6_if_A, prob6)
    print('Probability of type A = ', round(post_A, 4))


def bayesian_updating_bad_prior():
    prob_6_if_A = 1. / 5
    prob6 = (1.0 / 5 + 1.0 / 6 + 1.0 / 7) / 3
    prior_A = 0.9
    post_A = copy(prior_A)
    num_rolls = 200
    for i in range(0, num_rolls + 1):
        if i % (num_rolls // 10) == 0:
            print('After: ', i, 'rolls. Probability of type A = ',
                  round(post_A, 4))
        is_six = random.random() <= 1. / 7
        if is_six:
            post_A = calculate_bayes(post_A, prob_6_if_A, prob6)
        else:
            post_A = calculate_bayes(post_A, 1 - prob_6_if_A, 1 - prob6)

if __name__ == "__main__":
    # test_calculate_bayes()
    bayesian_updating_bad_prior()