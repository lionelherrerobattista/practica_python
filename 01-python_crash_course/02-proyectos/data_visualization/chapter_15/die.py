from random import randint

class Die():
    """Una clase que representa un dado."""
    
    def __init__(self, num_sides=6):
        """Asumir un dado de 6 caras"""
        self.num_sides = num_sides
        
    def roll(self):
        """Devuelve un valor aleatorio entre 1 y el número de caras."""
        return randint(1, self.num_sides)
