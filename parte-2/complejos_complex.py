# Números complejos
# Un número complejo esta compuesto por una parte real y una parte imaginaria

# Forma literal
numero_complejo = 2 - 3j
print('Contenido variable compleja:', numero_complejo)
print('El tipo de dato de la variable numero_compleko es:', type(numero_complejo))

print()

# Instancia de un número complejo apartir de la clase complex
numero_complejo = complex(2, 9)
print('Contenido variable compleja:', numero_complejo)
print('El tipo de dato de la variable numero_compleko es:', type(numero_complejo))

# Operaciones aritméticas sobre números complejos


suma = (2 - 3j) + (1 + 5j)
print('Suma: ', suma)

resta = (2 - 3j) - (1 + 5j)
print('Resta: ', resta)

producto = (2 - 3j) * complex(1,5)
print('Producto: ', producto)

division = (2 - 3j) / complex(1,5)
print('Division: ', division)


