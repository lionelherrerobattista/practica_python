import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try: #Cargo desde el archivo
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError: #si no existe 
        return None
    else:
        return username
        
def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj: #lo guardo
        json.dump(username, f_obj)
    return username
        
def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        message ="Is " + username + " your username? (y/n) " 
        answer = input(message)
        if answer == 'y':
            print("Welcome back, " + username + "!")
        else:
            get_new_username()
            print("We'll remember you when you come back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")


greet_user()
