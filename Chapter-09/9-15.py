"""
Lottery Analysis: You can use a loop to see how hard it might be to win the kind of 
lottery you just modeled. Make a list or tuple called my_ ticket. 
Write a loop that keeps pulling numbers until your ticket wins. 
Print a message reporting how many times the loop had to run to give you a winning ticket.
"""
from random import choice

tickets = (123, 234, 345, 456, 567, 678, 789, 890, 911, 922)
my_ticket = 789
attempts = 0

while True:
    attempts += 1
    ticket = choice(tickets)
    if ticket == my_ticket:
        break

print(f'It took {attempts} attempts to win the lottery.')
