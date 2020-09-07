# regress_to_mean
import matplotlib.pyplot as plt
from flip_coin import flip


def regress_to_mean(num_flips, num_trials):
    # get fraction of heads for each trial of num_flips
    frac_heads = []
    for t in range(num_trials):
        frac_heads.append(flip(num_flips))
    # find trials with extreme results and for each the next trial
    extremes, next_trials = [], []
    for i in range(len(frac_heads) - 1):
        if frac_heads[i] < 0.33 or frac_heads[i] > 0.66:
            extremes.append(frac_heads[i])
            next_trials.append(frac_heads[i + 1])
    # plot results
    plt.plot(range(len(extremes)), extremes, 'ko',
             label = 'Extreme')
    plt.plot(range(len(next_trials)), next_trials, 'k^',
             label = 'next trial')
    plt.axhline(0.5)
    plt.axhline(0.666, color = 'r')
    plt.axhline(0.333, color = 'r')
    plt.ylim(0, 1)
    plt.xlim(-1, len(extremes) + 1)
    plt.xlabel('Extreme Example and Next Trial')
    plt.ylabel('Fraction Heads')
    plt.title('Regression to the Mean')
    plt.legend(loc = 'best')
    plt.show()


if __name__ == '__main__':
    regress_to_mean(15, 100)