filename = 'guest_book.txt'

active = True

while(active):
    message = "\nEnter you name or write 'q' to exit: "
    guest = input(message)
    
    if(guest == 'q'):
        active = False
    else:
        print("Welcome " + guest + "!")
        with open(filename, 'a') as file_object:
            file_object.write(guest + "\n")

    
