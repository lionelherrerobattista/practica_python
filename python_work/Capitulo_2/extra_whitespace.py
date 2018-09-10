#Se puede sacar el espacio adicional en una cadena:
favorite_language = 'python '

print(favorite_language+"<-")
print(favorite_language.rstrip()+"<-")
#El método rstrip() no modifica la cadena almacenada:
print(favorite_language+"<-")
#Hay que guardarlo en la variable:
favorite_language = favorite_language.rstrip()
print(favorite_language+"<-")

#Para sacar de ambos lados strip()(solo izq.: lstrip()):
favorite_language = ' python '
print("->"+favorite_language.strip()+"<-")
