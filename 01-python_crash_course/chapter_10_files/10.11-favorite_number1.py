import json

filename = 'favorite_number.json'

with open(filename, 'w') as f_obj:
    favorite_number = input("Which is your favorite number? ")
    json.dump(favorite_number, f_obj)
