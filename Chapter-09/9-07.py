"""
Admin: An administrator is a special kind of user. 
Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 (page 162) or Exercise 9-5 (page
167). 
Add an attribute privileges, that stores a list of strings like "can add post"
"can delete post", "can ban user", and so on. 
Write a method called show_privileges () that lists the administrator's set of privileges. 
Create an instance of Admin, and call your method.
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

class Admin(User):

    def __init__(self, first_name, last_name, age, email):
        """Initializes admin attributes"""
        super().__init__(first_name, last_name, age, email)
        self.privileges = ["can add post","can delete post", "can ban user"]

    def show_privileges(self):
        """Print admin privileges"""
        for privilege in self.privileges:
            print(privilege)


admin = Admin('admin','', 20, 'admin@admin.com')
admin.show_privileges()