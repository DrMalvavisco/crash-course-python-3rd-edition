"""
6-12. Extensions: We're now working with examples that are complex enough that they can be extended in any number of ways. 
Use one of the example programs from this chapter, and extend it by adding new keys and values, 
changing the context of the program, or improving the formatting of the output."""


cities = {'mexico_city':{'country':'mexico','population':22.1,'fact':'The are a lot of chilangos.'},
        'paris':{'country':'france','population':11.4,'fact':'The house of Eiffel Tower.'},
        'madrid':{'country':'spain','population':3.2,'fact':'Here is the Santiago Bernabeu Stadium.'}
}

print("Cities that I've visited in 2021:")
for city,info in cities.items():
    print(f'City: {city.title()}\nCountry: {info["country"].title()}\nPopulation (in millions): {info["population"]}\nFact: {info["fact"]}\n')

print('One year later...\nCities that I\'ve visited in 2021, and 2022.')

for city in cities:
    cities[city]['year_visited'] = 2021

cities['moscu'] = {'country':'russia','population':11.2,'fact':'The are a lot of bears.', 'year_visited':2022}
cities['monterrey'] = {'country':'mexico','population':1.1,'fact':'The are a lot of carnita asada.', 'year_visited':2022}
cities['new_york'] = {'country':'usa','population':8.4,'fact':'The city that never sleeps.', 'year_visited':2022}

for city,info in cities.items():
    print(f'City: {city.title()}\nCountry: {info["country"].title()}\nPopulation (in millions): {info["population"]}\nFact: {info["fact"]}\nYear Visited: {info["year_visited"]}\n')
