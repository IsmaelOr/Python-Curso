# Números de punto flotante

import math

pi = 3.1416
precio = 29.95

print('Tipo de dato del valor pi: %s' % type(math.pi))

print('El valor de la variable math.pi es: %.6f' % pi)
print('El valor de la variable precio es: %.8f' % precio)

print(pi)
print(precio)

print()

print('Tipo de dato de la variable pi: ', type(pi))
print('Tipo de dato de la variable precio: ', type(precio))

# Operaciones aritméticas sobre números de punto flotante

pi = pi * 2
print('El nuevo valor de la variable pi es:', pi)

total = precio * 5
print('El total a pagar es: %.2f' % total)

# Uso de la clase float() para crear números de punto flotante

print('Creación de un número real (punto flotante) a partir de una cadena de caracteres: ')
precio_computadora = float(input('Ingrese el precio de la computadora: '))
print('El precio de la computadora es: $%.2f' % precio_computadora)
print('El tipo de dato de la variable precio_computadora es: %s' % type(precio_computadora))
