# plots.py
from Mortgages import Fixed
from Mortgages import FixedWithPts
from Mortgages import TwoRate

import matplotlib.pyplot as plt


def plot_mortgages(mortgages, amount):
    def __label_plot(figure, title, x_label, y_label):
        plt.figure(figure)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.legend(loc = 'best')
    
    styles = ['k-', 'k-.', 'k:']
    # give names to figure numbers
    payments, cost, balance, net_cost = 0, 1, 2, 3
    for i in range(0, len(mortgages)):
        plt.figure(payments)
        mortgages[i].plot_payments(styles[i])
        plt.figure(cost)
        mortgages[i].plot_to_pd(styles[i])
        plt.figure(balance)
        mortgages[i].plot_balance(styles[i])
        plt.figure(net_cost)
        mortgages[i].plot_net(styles[i])
    __label_plot(payments, 'Monthly Payments of $' + str(amount) +
        ' Mortgages', 'Months', 'Monthly Payments')
    __label_plot(cost, 'Cash Outlay of $' + str(amount) +
        ' Mortgages', 'Months', 'Total Payments')
    __label_plot(balance, 'Balance Remaining of $' + str(amount) +
        ' Mortgages', 'Months', 'Remaining Loan Balance of $')
    __label_plot(net_cost, 'Net Cost of $' + str(amount) + ' Mortgages',
        'Months', 'Payments - Equity $')


def compare_mortgages(amount, years, fixed_rate, pts, pts_rate,
                      var_rate_1, var_rate_2, var_months):
    total_months = years * 12
    fixed_1 = Fixed(amount, fixed_rate, total_months)
    fixed_2 = FixedWithPts(amount, pts_rate, total_months, pts)
    two_rate = TwoRate(amount, var_rate_2, total_months, var_rate_1, var_months)
    mortgages = [fixed_1, fixed_2, two_rate]
    for month in range(0, total_months):
        for mortgage in mortgages:
            mortgage.make_payment()
    plot_mortgages(mortgages, amount)


def test_compare_mortgages():
    compare_mortgages(20000, years = 400 // 12, fixed_rate = 0.07, pts = 3.25,
                      pts_rate = 0.05, var_rate_1 = 0.045, var_rate_2 = 0.095,
                      var_months = 48)
    

if __name__ == '__main__':
    test_compare_mortgages()
    plt.show()