# check_empirical.py
import random
from scipy import integrate

pi = 3.141592
e = 2.71828

def gaussian(x, mu, sigma):
    f = (1.0 / (sigma * ((2 * pi) ** 0.5)))
    g = e ** -(((x - mu)**2) / (2 * sigma ** 2))
    return f * g


def check_empirical(num_trials):
    for t in range(num_trials):
        mu = random.randint(-10, 10)
        sigma = random.randint(1, 10)
        print('For mu = ', mu, 'and sigma =', sigma)
        for num_std in (1, 2, 3):
            area = integrate.quad(gaussian, mu - num_std * sigma,
                                  mu + num_std * sigma,
                                  (mu, sigma))[0]
            print('  Fraction within', num_std, 'std = ',
                  round(area, 4))


if __name__ == '__main__':
    check_empirical(6)