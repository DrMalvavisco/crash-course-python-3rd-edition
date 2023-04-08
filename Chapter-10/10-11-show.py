""""
Favorite Number: Write a program that prompts for the user's favorite number. 
Use son. dumps () to store this number in a file. Write a separate program 
that reads in this value and prints the message "I know your favorite number! It's."
"""
from pathlib import Path
import json

path = Path('fav_number.json')
contents = path.read_text()
fav_number = json.loads(contents)

print(f'Your favorite number is {fav_number}')
