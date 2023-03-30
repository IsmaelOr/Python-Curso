# Tipo de dato compuesto diccionario (dict)
# Estructura: Clave - Valor

# Creación de diccionarios:
diccionario_1 = {
    'propiedad1': 1,
    'propiedad2': (1,2),
    'propiedad3': [1,2,3],
}

diccionario_2 = dict()
diccionario_2['propiedad1'] = 1
diccionario_2['propiedad2'] = (1,2)
diccionario_2['propiedad3'] = [1,2,3]

print(diccionario_1)
print(type(diccionario_1))
print()

print(diccionario_2)
print(type(diccionario_2))
print()

computadora = {
    'id': 1001,
    'marca': 'Hp',
    'ram': 16,
    'cpu': 'Intel Core i7',
    'almacenamiento': 1
}

print(computadora)
# Cantidad de propiedad de un diccionario
print(f'La variable diccionario `computadora` tiene {len(computadora)} propiedades')
print(f'El tipo de dato de la variable `computadora` es {type(computadora).__name__}')

print()

### Acceso individual a las propiedades y valores de un diccionario
# Acceso a los valores
# La clave debe ser identica, se distingue entre mayusculas y minusculas
print(f"ID: {computadora['id']}")
print(f"MARCA: {computadora['marca']}")
print(f"RAM: {computadora['ram']}")
print(f"CPU: {computadora['cpu']}")
print(f"ALMACENAMIENTO: {computadora['almacenamiento']}")

print()

# Para evitar error, si no se conocen las propiedades del diccionario, se puede usar get()
# diccionario.get('clave', 'valor_por_si_no_existe')
# No modifica las propiedades del diccionario.
print(computadora.get('GPU', '2070 Super'))
print(computadora)
print()

### Modificación del contenido de un diccionario
computadora['marca'] = 'MSi'
computadora['id'] = 2001
computadora['gpu'] = '2070 Super'
print('Diccionario `computadora` después de la modificación')
print(f"ID: {computadora['id']}")
print(f"MARCA: {computadora['marca']}")
print(f"RAM: {computadora['ram']}")
print(f"CPU: {computadora['cpu']}")
print(f"ALMACENAMIENTO: {computadora['almacenamiento']}")
print(f"GPU: {computadora['gpu']}")
print('Cantidad de propiedades del diccionario `computadora`:', len(computadora))

print()

### Iteración de un diccionario 
print('Iteración de un diccionario por medio de las llaves:')
for k in computadora.keys():
    print(f'{k.capitalize()}: {computadora[k]}')

print()

print('Iteración de un diccionario por medio de los valores:')
## Por medio de esta iteración no se conocen el nombre de las llaves
for v in computadora.values():
    print(v)

print()

#### ESTA ES LA MEJOR FORMA DE ITERAR UN DICCIONARIO
print('Iteración de un diccionario por medio de las llaves y valores:')
for k,v in computadora.items():
    print(f'{k.upper()}: {v}')

print()

### Métodos y operadores para variables de tipo diccionario:
## Uso de list() para convertir las llaves de un diccionario en una lista
llaves = list(computadora)
print(llaves)
print('Cantidad de llaves (atributos) del diccionario `computadora`:', len(computadora))

print()

## Uso de `in` para consultar si una llave se encuentra en un diccionario:
print('board' in computadora)
print('gpu' in computadora)
print()

## Remover una llave de un diccionario con pop() y extraer su valor
# computadora.pop('disquete')  # => ERROR La llave no existe en el diccionario
# diccionario.pop('llave', 'valor_por_si_no_existe_la_llave')
valor = computadora.pop('gpu')
print('Se ha removido la llave `gpu` del diccionario `computadora`.')
print('El valor de la llave `gpu` era:', valor)
print('gpu' in computadora)
print(computadora)
print()

valor = computadora.pop('gpu', 'Dispositivo no presente')
print(valor)
print()

## Remover una propiedad de un diccionario con popitem() y extraer su llave - valor (retorna una tupla)
# Se sigue un esquema LIFO (Last In - First Out)
print(computadora)
atributo = computadora.popitem()
print(f'Llave: {atributo[0]}')
print(f'Valor: {atributo[1]}')
print(computadora)

print()

## Uso del método reversed(), para invertir el orden de las propiedades de un diccionario
print(list(computadora))
print(list(reversed(computadora)))

print()

for k in computadora:
    print(f'{k.capitalize()}: {computadora[k]}')

print()

for k in reversed(computadora):
    print(f'{k.capitalize()}: {computadora[k]}')

print()

## Remover todos los elementos de un diccionario con el método clear()

print(f"Cantidad actual de llaves en el diccionario `computadora`:", len(computadora))
computadora.clear()
print(f"Cantidad actual de llaves en el diccionario `computadora` después de clear():", len(computadora))