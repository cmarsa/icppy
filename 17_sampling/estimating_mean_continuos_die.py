# estimating_mean_continuous_die.py
import random
import numpy as np
import matplotlib.pyplot as plt
from simplestats import variance, mean

def plot_means(num_dice_per_trial, num_dice_thrown, num_bins,
               legend, color, style):
    means = []
    num_trials = num_dice_thrown // num_dice_per_trial
    for i in range(num_trials):
        vals = 0
        for j in range(num_dice_per_trial):
            vals += 5 * random.random()
        means.append(vals / num_dice_per_trial)
    plt.hist(means, num_bins, color = color, label = legend,
             weights = np.array(len(means) * [1]) / len(means),
             hatch = style, edgecolor = 'k')
    return mean(means), variance(means)


def run_plot_means():
    mean_d, var = plot_means(1, 100000, 11, '1 die', 'w', '*')
    print('Mean of rolling 1 die =', round(mean_d, 4),
          'variance = ', round(var, 4))
    mean_d, var = plot_means(100, 100000, 11, 'Mean of 100 dice',
                           'w', '//')
    print('Mean of rolling 100 dice =', round(mean_d, 4),
          'Variance = ', round(var, 4))
    plt.title('Rolling continuous Dice')
    plt.xlabel('Value')
    plt.ylabel('Probability')
    plt.legend()
    plt.show()




if __name__ == '__main__':
    run_plot_means()