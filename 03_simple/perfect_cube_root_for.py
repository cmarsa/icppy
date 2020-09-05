# perfect_cube_root_for.py
# find the cube root of a perfect cube
x = int(input('Enter an integer: '))
for answer in range(0, abs(x) + 1):
    if answer ** 3 >= abs(x):
        break
if answer ** 3 != abs(x):
    print(x, 'is not a perfect cube')
else:
    if x < 0:
        answer = -answer
    print('Cube root of', x, 'is', answer)