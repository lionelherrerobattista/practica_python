def make_shirt(size, message):
    """Prints the size and the message on the t-shirt"""
    print("\nT-shirt size: " + size.upper())
    print("Message: " + message)
    
# Positional arguments:
make_shirt('M', "I love BA")

# Keyword arguments:
make_shirt(message = "I love BA", size = 'M')

