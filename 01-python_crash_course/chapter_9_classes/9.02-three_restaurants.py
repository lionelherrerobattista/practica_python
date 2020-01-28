class Restaurant():
    """A restaurant model"""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        """Describes the restaurant"""
        print("\nThe restaurant's name is " + self.restaurant_name.title() + ".")
        print("Its cuisine type is " + self.cuisine_type + ".")
    
    def open_restaurant(self):
        """Simulates restaurant opening"""
        print("The " + self.restaurant_name.title() +
            " retaurant is now open.")
        
restaurant = Restaurant('estilo campo', 'barbecue')
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant_two = Restaurant('sushi club', 'sushi')
restaurant_two.describe_restaurant()
restaurant_two.open_restaurant()    

restaurant_three = Restaurant('tandoor', 'Indian')
restaurant_three.describe_restaurant()
restaurant_three.open_restaurant()
