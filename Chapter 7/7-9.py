"""
7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure the sandwich
'past rami' appears in the list at least three times. 
Add code near the beginning of your program to print a message saying the deli has run out of pastrami, 
and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. 
Make sure no pastrami sandwiches end up in finished_sandwiches.
"""

sandwich_orders = ['chicken', 'past rami','egg', 'seafood', 'past rami', 'roast', 'grilled','past rami', 'ham']
finished_sandwiches = []

print('Ouh nouuuuuuh! Deli has run out of pastrami!')

while 'past rami' in sandwich_orders:
    sandwich_orders.remove('past rami')

while sandwich_orders:
    finished = sandwich_orders.pop()
    print(f'I made your {finished} sandwich.')
    finished_sandwiches.append(finished)

for finished_sandwich in finished_sandwiches:
    print(f'Sandwich made: {finished_sandwich}.')