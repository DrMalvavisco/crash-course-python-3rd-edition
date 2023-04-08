"""Stripping Names: Use a variable to represent a person's name, and include some whitespace characters at the beginning and end of the name.
Then print the name using each character combination, "\t" and "\n", at least once.

Print the name once, so the whitespace around the name is displayed. Then print the name using each of the three stripping functions, lstrip(),
rstrip(), and strip() """

name = "\t\t    \nLuis Zanabria\n\n\t    "
print(name)
print(f'Left Strip: {name.lstrip()}')
print(f'Right Strip: {name.rstrip()}')
print(f'Strip on both sides: {name.strip()}')