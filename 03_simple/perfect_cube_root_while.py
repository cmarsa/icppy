# cube_root.py
# find the cube root of a perfect cube
'''
The algorithmic technique used in this program is a variant of guess and
check called exhaustive enumeration. We enumerate all possibilities until we get
to the right answer or exhaust the space of possibilities.
'''
x = int(input('Enter an integer: '))
answer = 0

while answer ** 3 < abs(x):
    answer = answer + 1
if answer ** 3 != abs(x):
    print(x, 'is not a perfect cube.')
else:
    if x < 0:
        answer = -answer
    print('Cube root of', x, 'is', answer)
