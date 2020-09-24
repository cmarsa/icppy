# housing_plot.py
import numpy as np
import matplotlib.pyplot as plt

def plot_housing(impression):
    '''
    Assumes impression a str. Must be one of
        `flat`, `volatile`, `fair`
    Produce bar chart of housing prices over time
    '''
    f = open('input/midWestHousingPrices.txt', 'r')
    # each line of file contains year quarter prire
    # for MisWest region of US
    labels, prices = ([], [])
    for line in f:
        year, quarter, price = line.split()
        label = year[2:4] + '\n Q' + quarter[1]
        labels.append(label)
        prices.append(int(price) / 1000)
    quarters = np.arange(len(labels))
    width = 0.8
    plt.bar(quarters, prices, width)
    plt.xticks(quarters + width/2, labels)
    plt.title('Housing Prices in U.S. Midwest')
    plt.xlabel('Quarter')
    plt.ylabel('Average Price ($1,000\'s)')
    if impression == 'flat':
        plt.ylim(1, 500)
    elif impression == 'volatile':
        plt.ylim(180, 220)
    elif impression == 'fair':
        plt.ylim(150, 250)
        pass
    else:
        raise ValueError
    plt.show()


def test_plot_housing():
    plot_housing('flat')
    plot_housing('volatile')
    plot_housing('fair')


if __name__ == "__main__":
    test_plot_housing()