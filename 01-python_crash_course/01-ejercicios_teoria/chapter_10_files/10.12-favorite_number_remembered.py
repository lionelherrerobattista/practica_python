import json

def ask_favorite_number():
    filename = 'favorite_number.json'

    with open(filename, 'w') as f_obj:
        favorite_number = input("Which is your favorite number? ")
        json.dump(favorite_number, f_obj)
        
    return favorite_number
    
def get_stored_number():
    filename = 'favorite_number.json'
    try:
        with open(filename) as f_obj:
            favorite_number = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return favorite_number
        
def guess_favorite_number():
    favorite_number = get_stored_number()
    
    if favorite_number:
        print("I know your favorite number! It's " + favorite_number + ".")
    else:
       ask_favorite_number()
       
guess_favorite_number()
