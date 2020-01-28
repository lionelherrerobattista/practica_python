class User():
    """A user"""
    def __init__(self, first_name, last_name):
        """Initialize name and last name attributes"""
        self.first_name = first_name
        self.last_name = last_name
        
    def describe_user(self):
        """Prints a summary of the person's information"""
        print("\nFirst Name: " + self.first_name.title())
        print("Last Name: " + self.last_name.title())
        
    def greet_user(self):
        """Personalized greeting to the user"""
        print("\nHello " + self.first_name.title() + "!")
        
user_one = User('juan', 'gonzalez')
user_one.describe_user()
user_one.greet_user()

user_two = User('josé', 'lópez')
user_two.describe_user()
user_two.greet_user()
