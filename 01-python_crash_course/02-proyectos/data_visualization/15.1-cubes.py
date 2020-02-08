import matplotlib.pyplot as plt

# First 5:
# ~ x_values = list(range(1,6))

#First 5000:
x_values = list(range(1,5001))
y_values = [x**3 for x in x_values]



plt.scatter(x_values, y_values, s=40)

plt.title("Cube Numbers", fontsize=20)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)


plt.show()
