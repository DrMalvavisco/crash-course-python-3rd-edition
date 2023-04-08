"""
Silent Cats and Dogs: Modify your except block in Exercise 10-7 to fail silently if either file is missing.
"""

from pathlib import Path
files = ['dogs.txt', 'fishes.txt', 'cats.txt']

for file in files:
    path = Path(file)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        pass
    else:
        print(f'{"*"*10} {file} {"*"*10}')
        print(contents)
