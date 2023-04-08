"""
6-11. Cities: Make a dictionary called cities. 
Use the names of three cities as keys in your dic-tionary.
 Create a dictionary of information about each city and include the country that the city is in, 
 its approximate population, and one fact about that city. The keys for each city's dictionary should be something like country, 
 population, and fact. Print the name of each city and all of the information vou have stored about it.
"""

cities = {'mexico_city':{'country':'mexico','population':22.1,'fact':'The are a lot of chilangos.'},
        'paris':{'country':'france','population':11.4,'fact':'The house of Eiffel Tower.'},
        'madrid':{'country':'spain','population':3.2,'fact':'Here is the Santiago Bernabeu Stadium.'}
}

for city,info in cities.items():
    print(f'City: {city.title()}\nCountry: {info["country"].title()}\nPopulation (in millions): {info["population"]}\nFact: {info["fact"]}\n')