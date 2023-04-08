"""Verify User: The final listing for remember me.py assumes either that the user has already 
entered their username or that the program is running for the first time. 
We should modify it in case the current user is not the person who last used the program.
Before printing a welcome back message in greet_user (), ask the user if this 
is the correct username. If it's not, call get_new_username() to get the correct username."""

from pathlib import Path
import json


def get_stored_username(path):
    """Get stored username if available"""
    if path.exists():
        contents = path.read_text()
        user = json.loads(contents)
        return user

    return None


def get_new_user(path):
    """Prompt for a new user"""
    name = input('Input name: ')
    mail = input('Input mail: ')
    age = int(input('Input age: '))
    contents = json.dumps({'name': name, 'mail': mail, 'age': age})
    path.write_text(contents)
    return name


def greet_user(user):
    """Greets the user by name"""
    print(f"Hello again {user['name']}")


def verify_user():
    """Verify the current username"""
    path = Path('user.json')
    user = get_stored_username(path)
    if user:
        input_char = input(f"{user['name']}, is that correct (y,n)? ")
        if input_char in ['y', 'Y']:
            greet_user(user)
        else:
            name = get_new_user(path)
            print(f"We'll remember you when you come back, {name}")
    else:
        name = get_new_user(path)
        print(f"We'll remember you when you come back, {name}")


verify_user()
