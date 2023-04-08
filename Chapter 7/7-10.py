"""
7-10. Dream Vacation: Write a program that polls users about their dream vacation. 
Write a prompt similar to If you could visit one place in the world, where would you go? 
Include a block of code that prints the results of the poll.
"""

responses = {}
prompt = """If you could visit one place in the world, where would you go? """
polling_active = True

while polling_active:
    name = input('\nWhat is your name? ')
    response = input(prompt)

    responses[name] = response

    if input('Continue polling? (Y/n): ').lower() in ['n','no']:
        polling_active = False

print('\n----------Polling Results----------\n')
for name, response in responses.items():
    print(f'{name} would go to {response}.')