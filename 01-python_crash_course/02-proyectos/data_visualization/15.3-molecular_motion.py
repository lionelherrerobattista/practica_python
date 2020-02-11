import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    # Crea un random walk, y dibuja los puntos
    rw = RandomWalk(5000)
    rw.fill_walk()
    
    # Ajustar tamaño de la ventana
    plt.figure(dpi=128, figsize=(10, 6))
    
    point_numbers = list(range(rw.num_points)) # para pasárselo al estilo
    plt.plot(rw.x_values, rw.y_values, linewidth=1)
        
    # Resaltar el primer y el último punto
    plt.scatter(0, 0, c='green', edgecolors='none', s=100) # principio
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
        s=100)  # fin
        
    # Borro los ejes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    
    plt.show()
    
    
    
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
