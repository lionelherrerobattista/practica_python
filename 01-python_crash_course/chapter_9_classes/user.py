"""A set of classes that can be used to represent users in a website."""

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
        

        
