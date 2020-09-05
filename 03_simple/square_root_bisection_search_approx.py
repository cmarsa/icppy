# square_root_bisection_search_approx.py
epsilon = 0.01

x = float(input('Enter a non-negative float number: '))
num_guess = 0

if x > 0:
    low = 0.0
    high = max(1.0, x)
else:
    print('Enter a non-negative number.')
    exit()

answer = (high + low) / 2.0
while abs(answer ** 2 - x) >= epsilon:
    print('low = ', low, 'high = ', high, 'answer = ', answer)
    num_guess += 1
    if answer ** 2 < x:
        low = answer
    else:
        high = answer
    answer = (high + low) / 2.0
print('number of guesses: ', num_guess)
print(answer, 'is close to square root of', x)