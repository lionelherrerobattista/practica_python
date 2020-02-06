"""A class that represents an Admin and its privileges"""
from user import User

class Admin(User):
    """Administrator"""
    
    def __init__(self, first_name, last_name, privileges):
        super().__init__(first_name, last_name)
        self.privileges = Privileges(privileges)
        
class Privileges():
    
    def __init__(self, privileges):
        self.privileges = privileges
        
    def show_privileges(self):
        print("\nPrivileges: ")
        for privilege in self.privileges:
            print(privilege)
