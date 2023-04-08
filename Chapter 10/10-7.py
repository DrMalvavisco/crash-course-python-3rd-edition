"""
Addition Calculator: Wrap your code from Exercise 10-5 in a while loop 
so the user can continue entering numbers, 
even if they make a mistake and enter 
text instead of a number.
"""

sum = 0
while True:
    number = input('Number: ')
    if number in ['q', 'Q']:
        break
    try:
        number = int(number)
    except:
        print('Input numbers')
    else:
        sum += number
    finally:
        print(f'Sum: {sum}')
