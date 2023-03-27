# Tipo de dato int: Números enteros

puntaje = 300
x = -5

print(type(puntaje))
print(type(x))

print()

print('Puntaje antes de la adición: %i' % puntaje)
puntaje = puntaje + 50  # puntaje += 50
print('Puntaje después de la adición: %i' % puntaje)
print(type(puntaje))

print()

print('Valor de x antes de la adición: %i' % x)
x += 10
print('Valor de x después de la adición: %i' % x)
print(type(x))

print()

# Uso de la clase int() para crear números enteros

edad = int(input('Ingresa tu edad: '))
print('Tipo de dato de la variable edad: %s' % type(edad))

total_dias = edad * 365
print('Total de días vividos hasta el momento: %i' % total_dias)
