from user import User


class Privileges():

    def __init__(self):
        self.privileges_list = ["can add post",
                                "can delete post", "can ban user"]

    def show_privileges(self):
        """Print admin privileges"""
        for privilege in self.privileges_list:
            print(privilege)


class Admin(User):

    def __init__(self, first_name, last_name, age, email):
        """Initializes admin attributes"""
        super().__init__(first_name, last_name, age, email)
        self.privileges = Privileges()
