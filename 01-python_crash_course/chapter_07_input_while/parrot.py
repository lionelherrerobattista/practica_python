prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = '' # para que entre al while

active = True # flag
# ~ while message != 'quit':
while active: # mientras sea True
    message = input(prompt)
    
    if message == 'quit':
        active = False # para que termine el programa
    else:
        print(message)
