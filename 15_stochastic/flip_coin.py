# flip_coin.py
import random
import matplotlib.pyplot as plt
from simplestats import mean, variance, std_dev, cv

def flip(num_flips):
    '''
    Assumes num_flips a positive int
    '''
    heads = 0
    for i in range(num_flips):
        if random.choice(('H', 'T')) == 'H':
            heads += 1
    return heads / num_flips


def simulation_flip(num_flips_per_trial, num_trials):
    '''
    Assumes num_flips_per_trial and num_trials positive ints
    Returns simulation frac_heads, mean and std_dev
    '''
    frac_heads = []
    for i in range(num_trials):
        frac_heads.append(flip(num_flips_per_trial))
    simulation_mean = mean(frac_heads)
    simulation_std_dev = std_dev(frac_heads)
    return (frac_heads, simulation_mean, simulation_std_dev)


def flip_plot(min_exp, max_exp):
    '''
    Assumes min_exp and max_exp positive integers; min_exp < max_exp
    Plots results of 2**min_exp to 2**max_exp coin flips
    '''
    ratios, diffs, x_axis = [], [], []
    for exp in range(min_exp, max_exp + 1):
        x_axis.append(2 ** exp)
    for num_flips in x_axis:
        num_heads = 0
        for n in range(num_flips):
            if random.choice(('H', 'T')) == 'H':
                num_heads += 1
        num_tails = num_flips - num_heads
        try:
            ratios.append(num_heads / num_tails)
            diffs.append(abs(num_heads - num_tails))
        except ZeroDivisionError:
            continue
    plt.title('Difference Between Heads and Tails')
    plt.xlabel('Number of Flips')
    plt.ylabel('abs(#heads - #tails)')
    plt.plot(x_axis, diffs, 'ko')
    plt.figure()
    plt.title('Heads/Tails Ratios')
    plt.xlabel('Number of Flips')
    plt.ylabel('#heads / #tails')
    plt.plot(x_axis, ratios, 'ko')
    plt.show()


def make_plot(x_vals, y_vals, title, x_label, y_label, style,
              log_x = False, log_y = False):
    plt.figure()
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.plot(x_vals, y_vals, style)
    if log_x:
        plt.semilogx()
    if log_y:
        plt.semilogy()


def run_trial(num_flips):
    num_heads = 0
    for n in range(num_flips):
        if random.choice(('H', 'T')) == 'H':
            num_heads += 1
    num_tails = num_flips - num_heads
    return (num_heads, num_tails)


def flip_plot_mu_sig(min_exp, max_exp, num_trials):
    '''
    Assumes min_exp, max_exp, num_trials ints > 0;
        min_exp < max_exp
    Plots summaries of results of num_trials trials of
        2**min_exp to 2**max_exp coin flips
    '''
    ratios_means, diffs_means, ratios_sds, diffs_sds = [], [], [], []
    ratios_cvs, diffs_vcs = [], []
    x_axis = []
    for exp in range(min_exp, max_exp + 1):
        x_axis.append(2 ** exp)
    for num_flips in x_axis:
        ratios, diffs = [], []
        for t in range(num_trials):
            num_heads, num_tails = run_trial(num_flips)
            ratios.append(num_heads / num_tails)
            diffs.append(abs(num_heads - num_tails))
        ratios_means.append(sum(ratios) / num_trials)
        diffs_means.append(sum(diffs) / num_trials)
        ratios_sds.append(std_dev(ratios))
        diffs_sds.append(std_dev(diffs))
        ratios_cvs.append(cv(ratios))
        diffs_vcs.append(cv(diffs))
    num_trials_string = ' (' + str(num_trials) + ' Trials)'
    title = 'Mean Heads/Tails Ratios' + num_trials_string
    make_plot(x_axis, ratios_means, title, 'Number of flips',
              'Mean Heads/Tails', 'k.', log_x = True)
    title = 'SD Heads/Tails ratios' + num_trials_string
    make_plot(x_axis, ratios_sds, title, 'Number of Flips',
              'Standard Deviation', 'k.', log_x = True, log_y = True)
    title = 'Mean abs(#Heads - #Tails)' + num_trials_string
    make_plot(x_axis, diffs_means, title,'Number of Flips',
             'Mean abs(#Heads - #Tails)', 'k.', log_x = True, log_y = True)
    title = 'SD abs(#Heads - #Tails)' + num_trials_string
    make_plot(x_axis, diffs_sds, title, 'Number of Flips',
              'Standard Deviation', 'k.', log_x = True, log_y = True)
    title = 'Coeff. of Var. abs(#Heads - #Tails)' + num_trials_string
    make_plot(x_axis, diffs_vcs, title, 'Number of Flips',
              'Coeff. of Var.', 'k.', log_x = True)
    title = 'Coeff. of Var. Heads/Tails Ratio' + num_trials_string
    make_plot(x_axis, ratios_cvs, title, 'Number of Flips',
              'Coeff. of Var.', 'k.', log_x = True, log_y = True)
    plt.show()


def make_histograms(num_flips_1, num_flips_2, num_trials):
    '''
    '''
    def label_histogram(num_flips, num_trials, mean, sd):
        plt.title(str(num_trials) + ' trials of ' \
                      + str(num_flips) + ' flips each')
        plt.xlabel('Fraction of Heads')
        plt.ylabel('Number of Trials')
        plt.annotate('Mean = ' + str(round(mean, 4)) \
                     + '\nSD = ' + str(round(sd, 4)), size = 'x-large',
                     xycoords = 'axes fraction', xy = (0.67, 0.5))
    
    val_1, mean_1, sd1 = simulation_flip(num_flips_1, num_trials)
    plt.hist(val_1, bins = 20, color = 'gray', edgecolor = 'k')
    xmin, xmax = plt.xlim()
    label_histogram(num_flips_1, num_trials, mean_1, sd1)
    
    plt.figure()
    val_2, mean_2, sd2 = simulation_flip(num_flips_2, num_trials)
    plt.hist(val_2, bins = 20, color = 'gray', edgecolor = 'k')
    plt.xlim(xmin, xmax)
    label_histogram(num_flips_2, num_trials, mean_2, sd2)
    plt.show()


if __name__ == '__main__':
    # flip_plot_mu_sig(4, 20, 20)
    make_histograms(100, 1000, 100000)