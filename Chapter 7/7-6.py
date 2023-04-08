"""
7-6. Three Exits: Write different versions of either Exercise 7-4 or 7-5 that do each of the following at least once:
Use a conditional test in the while statement to stop the loop.
Use an active variable to control how long the loop runs.
Use a break statement to exit the loop when the user enters a 'quit' value.
"""
continuing = True

while continuing:
    age = int(input('What is your age?\n0 to stop: '))

    if age > 12:
        print('Your ticket cost is $15.')
    elif age >= 3:
        print('Your ticket cost is $10.')
    elif age > 0:
        print('Your ticket is free!')
    else:
        continuing = False
        #break another alternative