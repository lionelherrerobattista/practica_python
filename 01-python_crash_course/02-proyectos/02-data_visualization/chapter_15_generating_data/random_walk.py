from random import choice

class RandomWalk():
    """A class to generate random walks."""
    
    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points
        
        
        # All walks start at (0, 0)
        self.x_values = [0]
        self.y_values = [0]
        
    def get_step(self):
        axis_direction = choice([1, -1]) #izquierda o derecha
        axis_distance = choice([0, 1, 2, 3, 4]) #cantidad de pasos
        
        return axis_direction * axis_distance #calculo cuánto se mueve
            
        
    def fill_walk(self):
        """Calculate all the points in the walk."""
        
        # Keep taking steps until the walk reaches the desire length.
        while len(self.x_values) < self.num_points: # la cantidad de valores de x
            # La dirección y que tan lejos va en esa dirección
            
            
            x_step = self.get_step()
            
            y_step = self.get_step()
            
            # Descarto cuando no se mueve
            if x_step == 0 and y_step == 0:
                continue
                
            # Calculo los siguientes valores para x e y
            next_x = self.x_values[-1] + x_step # -1 toma el último valor de la lista
            next_y = self.y_values[-1] + y_step
            
            self.x_values.append(next_x)
            self.y_values.append(next_y)
            
