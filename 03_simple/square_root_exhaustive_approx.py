# square_root_exhaustive_approx.py
# Approximating the square root using exhaustive enumeration
'''
Exhaustive enumeration is a search technique that works only if the set of
values being searched includes the answer. In this case, we are enumerating the
values between 0 and the value of x . When x is between 0 and 1 , the square root
of x does not lie in this interval.
'''
epsilon = 0.01
step = epsilon ** 2

x = float(input('Enter a float number: '))
num_guess = 0
answer = 0
while(abs(answer ** 2 - x) >= epsilon and answer <= x):
    answer += step
    num_guess += 1
print('Number of guesses = ', num_guess)
if abs(answer ** 2 - x) >= epsilon:
    print('Failed on square root of', x)
else:
    print(answer, 'is close to square root of', x)