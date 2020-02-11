import pygal

from die import Die

# Crear dos D8.
die_1 = Die(8)
die_2 = Die(8)

# Tirar el dado y guardar los resultados en una lista.
results = []
for roll in range(5000000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
    
# Analizar los resultados.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualizar los resultados
hist = pygal.Bar() # Creo la instancia del grafico de barras

# etiquetas
hist.title = "Results of rolling two D8 dice 6000000 times."
hist.x_labels = list(range(2,17))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D8 + D8', frequencies) # agrego los valores al gráfico
hist.render_to_file('dice_visual8.svg')



