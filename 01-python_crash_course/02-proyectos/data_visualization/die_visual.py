import pygal

from die import Die

# Crear un D6.
die = Die()

# Tirar el dado y guardar los resultados en una lista.
results = []
for roll in range(1000):
    result = die.roll()
    results.append(result)
    
# Analizar los resultados.
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualizar los resultados
hist = pygal.Bar() # Creo la instancia del grafico de barras

# etiquetas
hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = list(range(1,7))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies) # agrego los valores al gráfico
hist.render_to_file('die_visual.svg')



