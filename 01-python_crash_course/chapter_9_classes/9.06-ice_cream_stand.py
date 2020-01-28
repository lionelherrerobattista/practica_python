class Restaurant():
    """A restaurant model"""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        """Describes the restaurant"""
        print("\nThe restaurant's name is " + self.restaurant_name.title() + ".")
        print("Its cuisine type is " + self.cuisine_type + ".")
        print("Clients served: " + str(self.number_served) + ".")
    
    def open_restaurant(self):
        """Simulates restaurant opening"""
        print("\nThe " + self.restaurant_name.title() +
            " retaurant is now open.")
            
    def set_number_served(self, number_served):
        """Sets the number of customers that have been served"""
        self.number_served = number_served
        
    def increment_number_served(self, customers):
        """Add the given amount to total customers"""
        self.number_served += customers
        
class IceCreamStand(Restaurant):
    
    def __init__(self, restaurant_name, cuisine_type, flavors):
        """Initializes ice cream stand"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
    
    def show_flavors(self):
        """Shows ice cream flavors of the restaurant"""
        print("\nThe restaurant flavors are:")
        for flavor in self.flavors:
            print("- " + flavor)
            

flavors = ['chocolate', 'cherry', 'banana']

ice_cream_stand = IceCreamStand('estilo campo', 'barbecue', flavors)
ice_cream_stand.show_flavors()
            
