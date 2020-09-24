# anorexics_and_june.py
import random

def june_prob(num_trials):
    june48 = 0
    for trial in range(num_trials):
        june = 0
        for i in range(0, 446):
            if random.randint(1, 12) == 6:
                june += 1
        if june >= 48:
            june48 += 1
    j_prob = round(june48/num_trials, 4)
    print('Probability of at least 48 births in june: ', j_prob)


def test_june_prob():
    june_prob(10000)


def any_prob(num_trials):
    any_month48 = 0
    for trial in range(0, num_trials):
        months = [0] * 12
        for i in range(0, 446):
            months[random.randint(0, 11)] += 1
        if max(months) >= 48:
            any_month48 += 1
    a_prob = round(any_month48 / num_trials, 4)
    print('Probability of at least 48 births in some month :', a_prob)


def test_any_prob():
    any_prob(10000)

if __name__ == '__main__':
    # test_june_prob()
    test_any_prob()
