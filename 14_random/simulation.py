# simulation.py
import matplotlib.pyplot as plt

from randomwalk import Field, OddField, Location
from randomwalk import UsualDrunk, EWDrunk, ColdDrunk
from randomwalk.plots import StyleIterator


def walk(f, d, num_steps):
    '''
    Assumes f a Field, d a Drunk in f, and num_steps an int >= 0.
    Moves d num_step times; returns the distance between the final
    location and the location at the start of the walk.
    '''
    start = f.get_loc(d)
    for s in range(0, num_steps):
        f.move_drunk(d)
    return start.dist_from(f.get_loc(d))


def simulate_walks(num_steps, num_trials, d_class):
    '''
    Assumes num_steps an int >= 0, num_trials an int > 0
        d_class a subclass of Drunk.
    Simulates num_trials walks of num_steps steps each.
    Returns a list of the final distances for each trial.
    '''
    homer = d_class()
    origin = Location(0, 0)
    distances = []
    for t in range(0, num_trials):
        f = Field()
        f.add_drunk(homer, origin)
        distances.append(round(walk(f, homer, num_steps), 1))
    return distances


def drunk_test(walk_lengths, num_trials, d_class):
    '''
    Assumes walk_lengths a sequence of ints >= 0
        num_trials an int > 0, d_class a subclass of Drunk
    For each number of steps in walk_lengths, runs simulate_walks
        with num_trials walks and prints results
    '''
    for num_steps in walk_lengths:
        distances = simulate_walks(num_steps, num_trials, d_class)
        print(d_class.__name__, 'random walk of', num_steps, 'steps')
        print('  mean: ', round(sum(distances) / len(distances), 4))
        print('  max: ', max(distances), 'min: ', min(distances))


def simulate_all(walk_lengths, num_trials, drunk_kinds):
    for d_class in drunk_kinds:
        drunk_test(walk_lengths, num_trials, d_class)


def simulate_drunk(walk_lengths, num_trials, d_class):
    mean_distances = []
    for num_steps in walk_lengths:
        print('   Starting simulation of', num_steps, 'steps')
        trials = simulate_walks(num_steps, num_trials, d_class)
        mean = sum(trials) / len(trials)
        mean_distances.append(mean)
    return mean_distances


def simulate_all_drunks(walk_lengths, num_trials, drunk_kinds):
    style_choice = StyleIterator(('m-', 'r:', 'k-.'))
    for d_class in drunk_kinds:
        current_style = style_choice.next_style()
        print('-Starting simulation of', d_class.__name__)
        means = simulate_drunk(walk_lengths, num_trials, d_class)
        plt.plot(walk_lengths, means, current_style, label = d_class.__name__)
    plt.title('Mean distance from origin (' \
                + str(num_trials) + ' trials)')
    plt.xlabel('Number of steps')
    plt.ylabel('Distance from origin')
    plt.legend(loc = 'best')
    plt.semilogx()
    plt.semilogy()
    plt.show()


def get_final_locations(num_steps, num_trials, d_class):
    locations = []
    d = d_class()
    for trial in range(0, num_trials):
        f = Field()
        f.add_drunk(d, Location(0, 0))
        for step in range(0, num_steps):
            f.move_drunk(d)
        locations.append(f.get_loc(d))
    return locations


def plot_locations(num_steps, num_trials, drunk_kinds):
    style_choice = StyleIterator(('k+', 'r^', 'mo'))
    for d_class in drunk_kinds:
        locations = get_final_locations(num_steps, num_trials, d_class)
        x_vals, y_vals = [], []
        for loc in locations:
            x_vals.append(loc.get_x())
            y_vals.append(loc.get_y())
        x_mean = sum(x_vals) / len(x_vals)
        y_mean = sum(y_vals) / len(y_vals)
        current_style = style_choice.next_style()
        plt.plot(x_vals, y_vals, current_style,
                 label = d_class.__name__ + ' mean loc. = <' \
                         + str(x_mean) + ', ' + str(y_mean) + '>')
    plt.title('Location at End of Walks (' \
              + str(num_steps) + ' steps)')
    plt.xlabel('Steps East/West of origin')
    plt.ylabel('Steps North/South of origin')
    plt.legend(loc = 'lower left')
    plt.show()


def trace_walk(num_steps, drunk_kinds):
    style_choice = StyleIterator(('k+', 'r^', 'mo'))
    f = Field()
    for d_class in drunk_kinds:
        d = d_class()
        f.add_drunk(d, Location(0, 0))
        locations = []
        for s in range(num_steps):
            f.move_drunk(d)
            locations.append(f.get_loc(d))
        x_vals, y_vals = [], []
        for loc in locations:
            x_vals.append(loc.get_x())
            y_vals.append(loc.get_y())
        current_style = style_choice.next_style()
        plt.plot(x_vals, y_vals, current_style,
                 label = d_class.__name__)
    plt.title('Spots visited on walk (' \
              + str(num_steps) + ' steps)')
    plt.xlabel('Steps East/West of Origin')
    plt.ylabel('Steps North/South of Origin')
    plt.legend(loc = 'best')
    plt.show()



def trace_walk_odd(num_steps, drunk_kinds):
    style_choice = StyleIterator(('k+', 'r^', 'mo'))
    f = OddField(100, 20, 20)
    for d_class in drunk_kinds:
        d = d_class()
        f.add_drunk(d, Location(0, 0))
        locations = []
        for s in range(num_steps):
            f.move_drunk(d)
            locations.append(f.get_loc(d))
        x_vals, y_vals = [], []
        for loc in locations:
            x_vals.append(loc.get_x())
            y_vals.append(loc.get_y())
        current_style = style_choice.next_style()
        plt.plot(x_vals, y_vals, current_style,
                 label = d_class.__name__)
    plt.title('Spots visited on walk (' \
              + str(num_steps) + ' steps)')
    plt.xlabel('Steps East/West of Origin')
    plt.ylabel('Steps North/South of Origin')
    plt.legend(loc = 'best')
    plt.show()

if __name__ == '__main__':
    # simulate all drunks
    # simulate_all_drunks((10, 100, 1000, 10000, 100000),
    #                     100,
    #                     (UsualDrunk, ColdDrunk, EWDrunk))

    # plot final locations
    # plot_locations(100, 200, (UsualDrunk, ColdDrunk, EWDrunk))
    
    # tracewall
    trace_walk_odd(200, (UsualDrunk, ColdDrunk, EWDrunk))
