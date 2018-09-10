#Crear una lista:
bicycles = ['trek','cannondale','redline','specialized']

print(bicycles) #Imprime la lista entre corchetes

#Accedo a los elementos indicando el subíndice
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])

#Para acceder al último elemento tambien se puede usar -1:
print(bicycles[-1])

#También sirve para acceder a los elementos en el sentido inverso:
print(bicycles[-2])

message = "My first bicycle was a " + bicycles[0].title() + "."
print("\n" + message)
