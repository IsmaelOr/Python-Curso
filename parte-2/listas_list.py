# Tipo de dato compuesto: lista
# Las listas son un tipo de dato dinámico, se puede modificar el contenido

# Creación de una lista:
numeros = [1,2,3,4,5,6,7]
print('Tipo de dato de la variable numeros:', type(numeros))
print('Cantidad de elementos:', len(numeros))
print('Contenido:', numeros)

print()

# Acceso a los elementos de una lista
primer_elemento = numeros[0]
ultimo_elemento = numeros[-1]

print('El primero elemento (índice 0) de la lista es:', primer_elemento)
print('El último elemento (índice -1) de la lista es:', ultimo_elemento)

ultimo_elemento = numeros[6]
print('El último elemento (índice 6) de la lista es:', ultimo_elemento)

print()

subseccion = numeros[1:4] # EL rango es abierto por la derecha, se debe aumentar en 1 hasta donde queremos llegar
print('Tipo de dato de la variable numeros:', type(subseccion))
print('Cantidad de elementos:', len(subseccion))
print('Contenido:', subseccion)

print()

## Acceso con desempaquetamiento:
print('Acceso a datos de una lista con desempaquetamiento:')
primer_elemento, segundo_elemento, tercer_elemento = subseccion
print(primer_elemento, segundo_elemento, tercer_elemento)
print()

## Acceso a un índice que no existe
# Izquierda a derecha: 0 hasta n-1
# Derecha a izquierda: -1 hasta -n
# valor = numeros[9]    => ERROR INDICE FUERA DE RANGO
# valor = numeros[-11]    => ERROR INDICE FUERA DE RANGO


### Modificar un elemento por medio del índice
print(numeros)
numeros[0] = 90
print(numeros)

### Modificar un elemento por medio de índices negativos
print(numeros)
numeros[-1] = 100
print(numeros)

print()

### Iteración de listas:
# Iteración de lista con ciclo while:
print('Iteración de lista con ciclo while:')
i = 0
while i < len(numeros):
    print(f'[{i}] - {numeros[i]}')
    i = i + 1

print()

# Iteración de lista con ciclo while (del último elemento al primero)
i = len(numeros) - 1
while i >= 0:
    print(f'[{i}] - {numeros[i]}')
    i = i - 1
print()

# Iteración de lista con ciclo for
print('Iteración con índices de una lista con un ciclo for:')
for i in range(0, len(numeros)):
    print(f'[{i}] - {numeros[i]}')

print()

# Iteración con índices de una lista con ciclo for (del último elemento al primero)

for i in range(len(numeros) - 1, -1):   ## Para que llegue al 0, se necesita poner -1
    print(f'[{i}] - {numeros[i]}')

print()

# Iteración por elemento de una lista con ciclo for (Sin acceso al índice)
print('Iteración con índices de una lista con un ciclo for each:')
for n in numeros:
    print(f'Valor: {n}')

print()

# Iteración de una lista por medio de enumerate()
print('Iteración con índices de una lista con enumerate():')
for i, v in enumerate(numeros):
    print(f'[{i}] - {v}')

print()

### Operaciones sobre listas (clase `list`)
# Inserción de elementos de una lista por medio de append()
print('Cantidad actual de elementos en la lista `numeros`: ', len(numeros))
numeros.append(14)
numeros.append(16)
print('Cantidad actual de elementos en la lista `numeros`: ', len(numeros))
print('Contenido actual de la lista `numeros`: ', numeros)

print()

# Inserción de elementos en una lista por medio de insert()
# lista.insert(indice, valor)
numeros.insert(1,19)
print('Contenido actual de la lista `numeros`: ', numeros)

numeros.insert(-1, 18)
print('Contenido actual de la lista `numeros`: ', numeros)

# Remover un elemento de una lista con la función remove()
# Valor que se desea eliminar (no indice)
numeros.remove(19)
print('Contenido actual de la lista `numeros`: ', numeros)
# numeros.remove(19)   => ERROR SI SE DESEA ELIMINAR UN ELEMENTO QUE NO EXISTE EN LA LISTA

print()

# Remover el último elemento de una lista con el método pop()
ultimo_elemento = numeros.pop()
print('Se ha eliminado el número: ', ultimo_elemento)
print('Contenido actual de la lista `numeros`: ', numeros)

print()

# Remover un elemento específico por medio de indice de una lista con el método pop()
elemento_eliminado = numeros.pop(1)
print('Se ha eliminado el número: ', elemento_eliminado)
print('Contenido actual de la lista `numeros`: ', numeros)

print()

# Remover un elemento específico por medio de su valor por medio de index() con el método pop()
eliminar_14 = numeros.pop(numeros.index(14))
print('Se ha eliminado el número: ', eliminar_14)
print('Contenido actual de la lista `numeros`: ', numeros)

print()

# numeros.pop(90)  => ERROR EL INDICE ESTA FUERA DEL RANGO EN LA LISTA

## Uso del método count() para contar las ocurrencias de un elemento en una lista:
print('Uso de count() en una lista:')
numeros.append(5)
numeros.append(5)
numeros.append(5)
ocurrencias = numeros.count(5)
print('Cantidad de veces que se halla 5 en la lista `numeros`: ', ocurrencias)

print()

ocurrencias = numeros.count(1)
print('Cantidad de veces que se halla 1 en la lista `numeros`: ', ocurrencias)

## Invertir los elementos de una lista (el ultimo se vuelve el primero, y el primero se vuelve el ultimo)
print('Contenido actual de la lista `numeros`: ', numeros)
numeros.reverse()   # Se modifica la lista sin necesidad de asignarla
print('Contenido actual de la lista `numeros` despues de reverse(): ', numeros)

print()

## Remover todos los elementos de una lista por medio de clear()
print('Cantidad actual de elementos en la lista `numeros`: ', len(numeros))
print('Contenido actual de la lista `numeros`: ', numeros)
numeros.clear()
print('Cantidad actual de elementos en la lista `numeros` después de clear(): ', len(numeros))
print('Contenido actual de la lista `numeros` después de clear(): ', numeros)

print()

## Remover todos los elmentos de una lista por medio de del
numeros = [1,2,3,4,5,6,7]
print('Cantidad actual de elementos en la lista `numeros`: ', len(numeros))
print('Contenido actual de la lista `numeros`: ', numeros)
del numeros[:]
print('Cantidad actual de elementos en la lista `numeros` después de `del`: ', len(numeros))
print('Contenido actual de la lista `numeros` después de `del`: ', numeros)


