"""Every Function: Think of thing you could store in a list.
For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you'd like.
Write a program that creates a list containing the items and then uses each function introduced in this chapter at least once."""

favorite_programming_languages = ['python','r','javascript','kotlin','scala','c','java']
print(f'Length of the list: {len(favorite_programming_languages)}')
print(f'1.- Favorite programming languages: {favorite_programming_languages}')
print(f'2.- Favorite programming languages in alphabetical order: {sorted(favorite_programming_languages)}')
print(f'3.- Favorite programming languages in reverse-alphabetical order: {sorted(favorite_programming_languages, reverse=True)}')
favorite_programming_languages.reverse()
print(f'4.- Favorite programming languages reverse list: {favorite_programming_languages}')
favorite_programming_languages.reverse()
print(f'5.- Favorite programming languages original list: {favorite_programming_languages}')
del favorite_programming_languages[6]
del favorite_programming_languages[5]
del favorite_programming_languages[4]
del favorite_programming_languages[3]
print(f'6.- Top 3 favorite programming languages:{favorite_programming_languages}')
favorite_programming_languages.sort()
print(f'7.- Top 3 favorite programming languages alphabetical order:{favorite_programming_languages}')
print(f'I like {favorite_programming_languages.pop().title()} because I love to use it in statistics applications.')
print(f'I like {favorite_programming_languages.pop().title()} because I use it for Data Analytics.')
print(f'I like {favorite_programming_languages.pop().title()} because I use it for Web Applications.')
print(f'Final list: {favorite_programming_languages}')
