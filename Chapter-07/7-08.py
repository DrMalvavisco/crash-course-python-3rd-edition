"""
7-8. Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches.
Then make an empty list called finished_sandwiches. 
Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. 
As each sandwich is made, move it to the list of finished sandwiches. 
After all the sandwiches have been made, print a message listing each sandwich that was made.
"""
sandwich_orders = ['chicken', 'egg', 'seafood', 'roast', 'grilled', 'ham']
finished_sandwiches = []

while sandwich_orders:
    finished = sandwich_orders.pop()
    print(f'I made your {finished} sandwich.')
    finished_sandwiches.append(finished)

for finished_sandwich in finished_sandwiches:
    print(f'Sandwich made: {finished_sandwich}.')