# Tipo de dato compuesto tupla - estático
# Las tuplas siguen el esquema de acceso basado en indices

punto = (2, 5)
print('Tipo de dato:', type(punto))
print('Contenido de la variable punto:', punto)
print('Cantidad de elementos de la tupla punto:', len(punto))

print()

# Acceso a los elementos(datos) de una tupla
x = punto[0]
y = punto[1]
print('El valor en x es igual a:', x)
print('El valor en y es igual a:', y)

print()

# Acceder a los datos por medio de Desempaquetamiento
abscisa, ordenada = punto
print('El valor en abscisa es igual a:', abscisa)
print('El valor en ordenada es igual a:', ordenada)

print()
# Acceder a los elementos del ultimo al primero, usando índices negativos (de derecha a izquierda)
penultimo_elemento = punto[-2]
ultimo_elemento = punto[-1]

print('El valor en x es igual a:', penultimo_elemento)
print('El valor en y es igual a:', ultimo_elemento)

print()

### Concepto de Inmutabilidad en una tupla (NO ES MODIFICABLE EL CONTENIDO DE LA TUPLA)
# punto[0] = 3   # ERROR EL OBJETO TUPLA NO SOPORTA MODIFICACIONES
# punto[1] = 7   # ERROR EL OBJETO TUPLA NO SOPORTA MODIFICACIONES

### Si se desea cambiar algo en la tupla se tiene que re-crear
punto = (3,7)
print('El valor en x es igual a:', punto[0])
print('El valor en y es igual a:', punto[1])

### Iteración de un objeto tipo tupla (tuple)
numeros_primos = (2,3,5,7,11,13,17,19)

print('Cantidad de elementos de la tupla numeros_primos:', len(numeros_primos))

print()

# Iteración con ciclo while:
print('Ciclo While')
i = 0
while i < len(numeros_primos):
    print(f'El valor del elemento en el índice {i} es igual a: {numeros_primos[i]}')
    i = i + 1

print()

# Iteración con ciclo for
print('Ciclo For')
for i in range(len(numeros_primos)):
    print(f'El valor del elemento en el índice {i} es igual a: {numeros_primos[i]}')

print()

# Iteración con un ciclo for mejorado: (No se tiene acceso a imprimir los índices, solo el contenido de la tupla)
print('Ciclo For Mejorado')
for p in numeros_primos:
    print(f'Valor: {p}')

print()

# Iteración de una tupla por medio de la función enumerate():
# i = indice, v = valor 
print('Iteración de la tupla numeros_primos con la función enumerate:')
for i,v in enumerate(numeros_primos):
    print(f'El valor del elemento en el índice {i} es igual a: {v}')

print()

### Mecanismso alternativos para crear una tupla:
# Modo con comas

numeros = 1,2,3
print('Tipo de datos de la variable numeros:', type(numeros))
print('Cantidad de elementos de la tupla:', len(numeros))
print('Contenido:', numeros)

# Crear una tupla de 1 elemento con comas
numeros = 1,
print('Tipo de datos de la variable numeros:', type(numeros))
print('Cantidad de elementos de la tupla:', len(numeros))
print('Contenido:', numeros)

print()

# Crear una tupla por medio de la clase tuple
impares = tuple([1,3,5])
print('Tipo de datos de la variable numeros:', type(impares))
print('Cantidad de elementos de la tupla:', len(impares))
print('Contenido:', impares)

print()

### Operaciones básicas que provee la clase `tuple`
print('Operaciones o métodos que provee la clase `tuple`')
colores = ('Negro', 'Blanco', 'Negro', 'Azul', 'Negro', 'Rojo', 'Verde')
print(colores.count('Negro'))
print(colores.count('negro')) ## Hace distinción entre mayusculas y minusculas
print(colores.index('Rojo'))
print(colores.index('Negro'))