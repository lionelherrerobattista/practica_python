def make_pizza(size, *toppings): #puedo pasar una cantidad indet. de argumentos
    """Print the list of toppings that have been requested."""
    print("\nMaking a " + str(size) +
    "-inch pizza with the following toppings:")
    for topping in toppings:# se guarda en una tupla
        print("- " + topping)

