"""
6-7. People: Start with the program you wrote for Exercise 6-1 (page 98). 
Make two new dictionaries representing different people, and store all three dictionaries in a list called people. 
Loop through your list of people. As you loop through the list, print everything you know about each person.
"""
person = {'first_name': 'Olga','last_name': 'Kolesnikova','age': '67','city': 'Moscu'}
person2 = {'first_name': 'Luka','last_name': 'Da Silva','age': '23','city': 'Rio du Janeiro'}
person3 = {'first_name': 'Ignacio','last_name': 'Varga','age': '25','city': 'Albuquerque'}

personas = [person, person2, person3]
for persona in personas:
    print("****************************************************")
    print(f"First name: {persona['first_name']}\nLast name: {persona['last_name']}\nAge: {persona['age']}\nCity: {persona['city']} ")