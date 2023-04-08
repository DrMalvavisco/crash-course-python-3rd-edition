"""User Dictionary: The remember_me.py example only stores one piece of information, the username. 
Expand this example by asking for two more pieces of information about the user, then store 
all the information you collect in a dictionary.
Write this dictionary to a file using json.dumps(), and read it back in using json.loads (). 
Print a summary showing exactly what your program remembers about the user."""


from pathlib import Path
import json

path = Path('user.json')
if path.exists():
    contents = path.read_text()
    user = json.loads(contents)
    print(f"User: {user['name']}, Mail: {user['mail']}, Age: {user['age']}")
else:
    name = input('Input name: ')
    mail = input('Input mail: ')
    age = int(input('Input age: '))
    contents = json.dumps({'name': name, 'mail': mail, 'age': age})
    path.write_text(contents)
