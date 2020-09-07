# exponential_decay.py
import matplotlib.pyplot as plt


def clear(n, p, steps):
    '''
    Assumes n & steps positive ints, p a float
        n: the initial number of molecules
        p: the probability of a molecule being cleared
        steps: the length of the simulation
    '''
    num_remaining = [n]
    for t in range(steps):
        num_remaining.append(n * ((1 - p) ** t))
    plt.plot(num_remaining, 'k--')
    plt.xlabel('Time')
    plt.ylabel('Molecules remaining')
    plt.title('Clearence of drug')
    plt.show()


if __name__ == '__main__':
    clear(1000, 0.01, 1000)