filename = 'programming_poll.txt'

active = True

while(active):
    message = "\nWhy you like programming? (write 'q' to exit)\n"
    reason = input(message)
    
    if(reason == 'q'):
        active = False
    else:
        with open(filename, 'a') as file_object:
            file_object.write(reason + "\n")
