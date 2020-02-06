guest = input("Enter your name: ")

filename = 'guest.txt'

with open(filename, 'a') as file_object:
    file_object.write(guest)
