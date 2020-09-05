# sum_string_csv.py
'''
Let s be a string that contains a sequence of decimal numbers
separated by commas, e.g., s = '1.23,2.4,3.123' . Write a program that prints the
sum of the numbers in s .
'''
string = input('Enter a string of numbers separated by a comma: ')
numbers = map(float, string.split(','))
sum = 0
for number in numbers:
    sum += number
print('Total sum of number is: ', sum)