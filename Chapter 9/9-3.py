"""
Users: Make a class called User. 
Create two attributes called first_name and last_name, 
and then create several other attributes that are typically stored in a user profile.
Make a method called describe_user () that prints a summary of the user's information.
Make another method called greet _user () that prints a personalized greeting to the user.
Create several instances representing different users, and call both methods for each user.
"""

class User:
    """A class that defines a User."""

    def __init__(self, first_name, last_name, age, email):
        """Initializes a user with first name, last name, age, and email."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def describe_user(self):
        """Prints user details."""
        print(f'First Name: {self.first_name.title()}')
        print(f'Last Name: {self.last_name.title()}')
        print(f'Age: {self.age}')
        print(f'Email: {self.email}')

    def greet_user(self):
        """Greets the user."""
        print(f'Hello! {self.first_name.title()} {self.last_name.title()}')
        

users = [
        User('Luis', 'Zanabria', 24, 'luis@zanabria.com'),
        User('Luka', 'Modric', 34,'luka@modric.com' ),
        User('Jorge', 'Mendoza', 50, 'jorge@mendoza.com'),
        User('Veronica', 'Vega', 24, 'veronica@vega.com'),
        User('Natalia', 'Lafourcade', 40, 'natalia@lafourcade.com')
]

for user in users:
    user.describe_user()
    user.greet_user()




        