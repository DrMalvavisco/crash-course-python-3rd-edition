"""
6-6. Polling: Use the code in favorite languages.py (page 96).
Make a list of people who should take the favorite languages poll. 
Include some names that are already in the dictionary and some that are not.
Loop through the list of people who should take the poll. 
If they have already taken the poll, print a message thanking them for responding. 
If they have not yet taken the poll, print a message inviting them to take the poll.
"""

people = ['ramses','juana','luka','chiqui']

favorite_programming_languages = {'nicole':'python','omar':'r','juana':['javascript','kotlin'],'chicoche':'scala','luka':['c','java']}

for name in people:
    if name in favorite_programming_languages.keys():
        print(f'Thanks for taking the poll, {name.title()}.')
    else:
        print(f'You should take the poll, {name.title()}.')

