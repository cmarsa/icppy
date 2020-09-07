# geometric_dist.py
import random
import matplotlib.pyplot as plt

def successful_starts(success_prob, num_trials):
    '''
    Assumes succes_prob is a float representing probability of a 
        single attempt being successful. numt_trials a positive int
    Returns a lust of the number of attempts needed before a 
        success for each trial.
    '''
    tries_before_success = []
    for t in range(0, num_trials):
        consec_failures = 0
        while random.random() > success_prob:
            consec_failures += 1
        tries_before_success.append(consec_failures)
    return tries_before_success


def test_successfuul_starts():
    prob_of_success = 0.5
    num_trials = 5000
    distribution = successful_starts(prob_of_success, num_trials)
    plt.hist(distribution, bins = 14, color = 'gray', edgecolor = 'k')
    plt.xlabel('Tries before success')
    plt.ylabel('Number of OCcurrences Out of ' + str(num_trials))
    plt.title('Probability of starting each try: ' + str(prob_of_success))
    plt.show()


if __name__ == '__main__':
    test_successfuul_starts()
