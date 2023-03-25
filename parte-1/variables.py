# Los nombres de las variables deben ser significados a su valor, para poder saber de que tratan

edad = 29
dias_vividos = edad * 365

print(edad)
print(dias_vividos)

# Obtener el tipo de dato

print('Tipo de dato de la variavke edad:',type(edad))
print('Tipo de dato de la variavke dias_vividos:',type(dias_vividos))

# Posicion en memoria de las variables

print('Posicion en memoria de la variable edad:', id(edad))
print('Posicion en memoria de la variable dias_vividos:', id(dias_vividos))


print('Posicion en memoria del valor 29:', id(29))
print('Posicion en memoria del valor 10585', id(10585))