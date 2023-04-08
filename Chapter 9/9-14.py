"""
Lottery: Make a list or tuple containing a series of 10 numbers and 5 letters. 
Randomly select 4 numbers or letters from the list and print a message saying that any 
ticket matching these 4 numbers or letters wins a prize.
"""
from random import choice

tickets = (123, 234, 345, 456, 567, 678, 789, 890, 911, 922)

for winner in range(4):
    print(f'Winner ticket: {choice(tickets)}')
