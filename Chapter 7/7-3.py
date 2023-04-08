"""
7-3. Multiples of Ten: Ask the user for a number, and then report whether the number is a multiple of 10 or not.
"""

number = int(input('Number: '))
if number % 10 == 0 :
    print(f'{number} is multiple of 10')
