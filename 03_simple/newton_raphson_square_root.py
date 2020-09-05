# newton_raphson_square_root.py
# find x such that x**2 - y is whithin epsilon of 0
epsilon = 0.01
y = float(input('Enter a non-negative float number: '))
guess = y / 2.0
num_guess = 0
while abs(guess * guess - y) >= epsilon:
    print('current guess: ', guess)
    num_guess += 1
    guess = guess - (((guess ** 2) - y) / (2 * guess))
print('Total number of guesses: ', num_guess)
print('Suare root of', y, 'is about', guess)