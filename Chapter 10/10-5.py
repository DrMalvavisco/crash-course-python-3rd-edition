"""
Guest Book: Write a while loop that prompts users for their name. 
Collect all the names that are entered, and then write these names to a file called guest_book.txt. 
Make sure each entry appears on a new line in the file.
"""
from pathlib import Path
path = Path('guest_book.txt')
content = ''

while True:
    guest = input('Name of guest (q for exit): ')

    if guest in ['q', 'Q']:
        break

    content += guest + '\n'

path.write_text(content)
