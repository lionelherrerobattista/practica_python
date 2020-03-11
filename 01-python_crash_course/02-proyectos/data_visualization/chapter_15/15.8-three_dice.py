import pygal

from die import Die

# Crear tres D6.
die_1 = Die(6)
die_2 = Die(6)
die_3 = Die(6)

# Tirar el dado y guardar los resultados en una lista.
results = []
for roll in range(1000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)
    
# Analizar los resultados.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualizar los resultados
hist = pygal.Bar() # Creo la instancia del grafico de barras

# etiquetas
hist.title = "Results of rolling three D6 dice 1000 times."
hist.x_labels = list(range(3,max_result+1))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6 + D6', frequencies) # agrego los valores al gráfico
hist.render_to_file('dice_visual3.svg')
