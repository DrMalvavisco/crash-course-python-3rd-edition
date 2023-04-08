"""
6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. 
In each dictionary, include the kind of animal and the owner's name. 
Store these dictionaries in a list called pets. 
Next, loop through your list and as you do, print everything you know about each pet.
"""

pet = {'kind':'dog', 'owner':'patrick'}
pet2 = {'kind':'cat', 'owner':'luis'}
pet3 = {'kind':'frog', 'owner':'jessica'}
pet4 = {'kind':'cat', 'owner':'luka'}
pet5 = {'kind':'lion', 'owner':'jamal'}

pets = [pet, pet2, pet3, pet4, pet5]

for pettie in pets:
    print(f'This pet is a {pettie["kind"]} and the owner is {pettie["owner"]}.\n')