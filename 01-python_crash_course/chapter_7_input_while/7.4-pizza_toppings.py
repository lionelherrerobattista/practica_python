prompt = "\nEnter your pizza topping:"
prompt += "\n(Type 'quit' to exit) "

topping = ''

while topping != 'quit':
    topping = input(prompt)
        
    if topping != 'quit':
        print("\nAdding " + topping.lower() + " to the pizza!")
