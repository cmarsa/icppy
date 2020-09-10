# projectile.py
import io
import numpy as np
import matplotlib.pyplot as plt


def get_trajectory_data(file_name):
    data_file = io.open(file_name, 'r')
    distances = []
    heights_1, heights_2, heights_3, heights_4 = [], [], [], []
    data_file.readline()
    for line in data_file:
        d, h1, h2, h3, h4 = line.split()
        distances.append(float(d))
        heights_1.append(float(h1))
        heights_2.append(float(h2))
        heights_3.append(float(h3))
        heights_4.append(float(h4))
    data_file.close()
    return (distances, [heights_1, heights_2, heights_3, heights_4])


def process_trajectories(file_name = 'input/trajectory_data.txt'):
    distances, heights = get_trajectory_data(file_name)
    num_trials = len(heights)
    distances = np.array(distances)
    # get array containing mean height at each distance
    tot_heights = np.array([0] * len(distances))
    for h in heights:
        tot_heights = tot_heights + np.array(h)
    mean_heights = tot_heights / len(heights)
    plt.title('Trajectory of Projectile (Mean of '\
                + str(num_trials) + ' Trials)')
    plt.xlabel('Inches from Launch Point')
    plt.ylabel('Inches Above Launch Point')
    plt.plot(distances, mean_heights, 1)
    fit = np.polyfit(distances, mean_heights, 1)
    altitudes = np.polyval(fit, distances)
    r_sq = r_squared(mean_heights, altitudes)
    plt.plot(distances, altitudes, 'b', label = f'Linear fit: {r_sq:.4f}')
    fit = np.polyfit(distances, mean_heights, 2)
    altitudes = np.polyval(fit, distances)
    r_sq = r_squared(mean_heights, altitudes)
    plt.plot(distances, altitudes, 'k:', label = f'Quadratic fit: {r_sq:.4f}')
    plt.legend()
    plt.show()


def r_squared(measured, predicted):
    '''
    Assumes measured a one-dimensional arrya of measured values
            predicted a one-dimensional array of prediced values
    Returns coefficient of determination
    '''
    estimate_error = ((predicted - measured) ** 2).sum()
    mean_of_measured = measured.sum() / len(measured)
    variability = ((measured - mean_of_measured) ** 2).sum()
    return 1 - estimate_error/variability


def get_horizontal_speed(quad_fit, min_x, max_x):
    '''
    Assumes quad_fit has coefficients of a quadratic polynomial
            min_x and max_x are distances in inches
    Returns horizontal speed in feer per second.
    '''
    inches_per_foot = 12
    x_mid = (max_x - min_x) / 2
    a, b, c = quad_fit[0], quad_fit[1], quad_fit[2]
    y_peak = a * x_mid ** 2 + b * x_mis + c
    g = 32.16 * inches_per_foot
    t = (2 * y_peak / g) ** 0.5
    print('Horizontal speed: ', int(x_mid/(t * inches_per_foot)), 'feet/sec')


if __name__ == "__main__":
    process_trajectories()
