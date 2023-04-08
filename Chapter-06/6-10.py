"""
6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 98) so each person can have more than one favorite number. 
Then print each person's name along with their favorite numbers.
"""

favs = {'Rowena':[5,2,9],'Max':[88],'Gina':[7,77,777,7777],'Mia':[14, 11],'Manuel':[18]}

for k,v in favs.items():
    print(f'My name is {k} and my fav. numbers are {v}')