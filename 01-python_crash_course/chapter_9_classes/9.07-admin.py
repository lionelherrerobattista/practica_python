class User():
    """A user"""
    def __init__(self, first_name, last_name):
        """Initialize name and last name attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
        
    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0
        
    def get_login_attempts(self):
        return self.login_attempts
        
    def describe_user(self):
        """Prints a summary of the person's information"""
        print("\nFirst Name: " + self.first_name.title())
        print("Last Name: " + self.last_name.title())
        
    def greet_user(self):
        """Personalized greeting to the user"""
        print("\nHello " + self.first_name.title() + "!")
        
class Admin(User):
    """Administrator"""
    
    def __init__(self, first_name, last_name, privileges):
        super().__init__(first_name, last_name)
        self.privileges = privileges
        
    def show_privileges(self):
        print("\nPrivileges: ")
        for privilege in privileges:
            print(privilege)
        
user_one = User('juan', 'gonzalez')
user_one.describe_user()
user_one.increment_login_attempts()
user_one.increment_login_attempts()
user_one.increment_login_attempts()

login_attempts = user_one.get_login_attempts()
print("\nLogin attempts: " + str(login_attempts))
print("\nResetting login attempts...")
user_one.reset_login_attempts()
login_attempts = user_one.get_login_attempts()
print("Login attempts: " + str(login_attempts))

user_one.greet_user()

# ~ user_two = User('josé', 'lópez')
# ~ user_two.describe_user()
# ~ user_two.greet_user()

privileges = ["can add post", "can delete post", "can ban user"]
admin = Admin('josé', 'lopez', privileges)
admin.show_privileges()
