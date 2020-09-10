# spring.py
import io
import numpy as np
import matplotlib.pyplot as plt


def get_spring_data(file_name):
    data_file = io.open(file_name, 'r')
    distances = []
    masses = []
    data_file.readline()
    for line in data_file:
        d, m = line.split(' ')
        distances.append(float(d))
        masses.append(float(m))
    data_file.close()
    return (masses, distances)


def plot_spring_data(input_file = 'input/spring_data.txt'):
    masses, distances = get_spring_data(input_file)
    distances = np.array(distances)
    masses = np.array(masses)
    forces = masses * 9.81
    plt.plot(forces, distances, 'bo',
             label = 'Measured displacements')
    plt.title('Measured Displacement of Spring')
    plt.xlabel('|Force| (Newtons)')
    plt.ylabel('Distance (meters)')
    plt.show()


def fit_spring_data(input_file = 'input/spring_data.txt'):
    masses, distances = get_spring_data(input_file)
    distances = np.array(distances)
    masses = np.array(masses)
    forces = masses * 9.81
    plt.plot(forces, distances, 'ko',
             label = 'Measured displacements')
    plt.title('Measured Displacement of Spring')
    plt.xlabel('|Force| (Newtons)')
    plt.ylabel('Distance (meters)')
    # find linear fit
    a, b = np.polyfit(forces, distances, 1)
    predicted_distances = a * np.array(forces) + b
    k = 1.0 / a
    plt.plot(forces, predicted_distances,
             label = 'Displacements predicted by\nlinear fit, k = ' \
                     + str(round(k, 4)))
    plt.legend(loc = 'best')
    # find cubic fit
    fit = np.polyfit(forces, distances,3)
    predicted_distances = np.polyval(fit, forces)
    plt.plot(forces, predicted_distances, 'k:',
             label = 'Displacements predicted by\ncubic fit, k = ' \
                     + str(round(k, 4)))
    plt.legend(loc = 'best')
    plt.show()


if __name__ == '__main__':
    fit_spring_data()
