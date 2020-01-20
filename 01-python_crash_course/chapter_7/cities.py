prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True: # se ejecuta para siempre
    city = input(prompt)
    
    if city == 'quit':
        break # termina la ejecución del bucle
    else:
        print("I'd love to go to " + city.title() + "!")


