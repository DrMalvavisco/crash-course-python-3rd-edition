"""
6-2. Favorite Numbers: Use a dictionary to store people's favorite numbers. 
Think of five names, and use them as keys in your dictionary. 
Think of a favorite number for each person, and store each as a value in your dictionary. 
Print each person's name and their favorite num-ber. 
For even more fun, poll a few friends and get some actual data for your program.
"""

favs = {'Rowena':5,'Max':88,'Gina':7,'Mia':14,'Manuel':18}

for k,v in favs.items():
    print(f'My name is {k} and my fav. number is {v}')