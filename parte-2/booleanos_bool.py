# Tipo de datos booleanos [True,False]
# Falso = False
# Verdadero = True

llueve = False

print('El tipo de dato de la variable llueve: ', type(llueve))
print(llueve)

if llueve:
    print('El día esta lluvioso')
else:
    print('El día esta soleado')

# Negar un valor bool

llueve = not llueve
print('Resultado despues de negar llueve: ', llueve)

# Los booleanos son utiles para crear condiciones

if llueve:
    print('El día esta lluvioso')
else:
    print('El día esta soleado')

# Operaciones con variables o valores booleanos (lógicos):

llave_1 = True
llave_2 = False

# Operadores lógicos: and, or
print( llave_1 and llave_2)
print( llave_1 and not llave_2)
print( llave_1 or llave_2)
print(not llave_1 or llave_2)

print()

# Si a y b son 2 llaves de agua, mostrar si hay agua

if llave_1 or llave_2:
    print('Si hay agua')
else:
    print('No hay agua')

print()

# Si alguna de las dos llaves esta cerrada, no sale agua

if llave_1 and llave_2:
    print('Si hay agua')
else:
    print('No hay agua')

# Instancia de un booleano apartir de la clase bool

print()

x = bool(1)   # TRUE
print(x)
print('El tipo de dato de la variable x es:', type(x))

x = bool(123)  # TRUE
print(x)
print('El tipo de dato de la variable x es:', type(x))

x = bool(-21) # TRUE
print(x)
print('El tipo de dato de la variable x es:', type(x))

x = bool(0) # FALSE
print(x)
print('El tipo de dato de la variable x es:', type(x))

x = bool('False') # TRUE
print(x)
print('El tipo de dato de la variable x es:', type(x))

x = bool('True') # TRUE
print(x)
print('El tipo de dato de la variable x es:', type(x))

x = bool(True) # TRUE
print(x)
print('El tipo de dato de la variable x es:', type(x))

x = bool(False) # FALSE
print(x)
print('El tipo de dato de la variable x es:', type(x))

x = bool(123 < 124) # TRUE
print(x)
print('El tipo de dato de la variable x es:', type(x))

x = 90 == 9 # FALSE
print(x)
print('El tipo de dato de la variable x es:', type(x))