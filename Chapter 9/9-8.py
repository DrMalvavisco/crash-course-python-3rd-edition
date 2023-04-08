"""
Privileges: Write a separate Privileges class. 
The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7. 
Move the show_privileges() method to this class.
Make a Privileges instance as an attribute in the Admin class. 
Create a new instance of Admin and use your method to show its privileges.
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

class Privileges():

    def __init__(self):
        self.privileges_list = ["can add post","can delete post", "can ban user"]

    def show_privileges(self):
        """Print admin privileges"""
        for privilege in self.privileges_list:
            print(privilege)

class Admin(User):

    def __init__(self, first_name, last_name, age, email):
        """Initializes admin attributes"""
        super().__init__(first_name, last_name, age, email)
        self.privileges = Privileges()


admin = Admin('admin','', 20, 'admin@admin.com')
admin.privileges.show_privileges()

    

