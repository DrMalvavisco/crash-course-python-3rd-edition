"""
9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3 (page 162). 
Write a method called increment_ login_attempts () that increments the value of login_attempts by 1. 
Write another method called reset_login_attempts () that resets the value of login_attempts to 0.
Make an instance of the User class and call increment_login_attempts () several times.
Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts ().
Print login_attempts again to make sure it was reset to 0.
"""

class User:
    """A class that defines a User."""

    def __init__(self, first_name, last_name, age, email):
        """Initializes a user with first name, last name, age, and email."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        """Prints user details."""
        print(f'First Name: {self.first_name.title()}')
        print(f'Last Name: {self.last_name.title()}')
        print(f'Age: {self.age}')
        print(f'Email: {self.email}')

    def greet_user(self):
        """Greets the user."""
        print(f'Hello! {self.first_name.title()} {self.last_name.title()}')
    
    def increment_login_attempts(self):
        """Increment login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login attempts to 0."""
        self.login_attempts = 0


user = User('juan', 'son', 30, 'juan@son.com')

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

print(f'Login attempts for user {user.first_name.title()} {user.last_name.title()}: {user.login_attempts}')
user.reset_login_attempts()
print(f'Login attempts for user {user.first_name.title()} {user.last_name.title()}: {user.login_attempts}')
