# world_series_simulation.py
import random
import matplotlib.pyplot as plt

def play_series(num_games, team_prob):
    num_won = 0
    for game in range(num_games):
        if random.random() <= team_prob:
            num_won += 1
    return (num_won > num_games // 2)


def fraction_won(team_prob, num_series, series_len):
    won = 0
    for series in range(num_series):
        if play_series(series_len, team_prob):
            won += 1
    return won / float(num_series)


def simulate_series(num_series):
    prob = 0.5
    fracs_won, probs = [], []
    while prob <= 1.0:
        fracs_won.append(fraction_won(prob, num_series, 7))
        probs.append(prob)
        prob += 0.01
    plt.axhline(0.95)
    plt.plot(probs, fracs_won, 'k', linewidth = 3)
    plt.xlabel('Probability of Winning a Game')
    plt.ylabel('Probability of Winning a Series')
    plt.title(str(num_series) + ' Seven-Game Series')
    plt.show()


if __name__ == '__main__':
    simulate_series(400)