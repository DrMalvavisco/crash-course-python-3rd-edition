"""
Addition: One common problem when prompting for numerical input occurs when people 
provide text instead of numbers. 
When you try to convert the input to an int, you'll get a ValueError. 
Write a program that prompts for two numbers. 
Add them together and print the result. 
Catch the ValueError if either input value is not a number, 
and print a friendly error message. 
Test your program by entering two numbers and 
then by entering some text instead of a number.
"""

try:
    num_1 = int(input('Number 1: '))
    num_2 = int(input('Number 2: '))
except ValueError:
    print('Please, input numbers')
else:
    print(f'{num_1} + {num_2} = {num_1+num_2}')
