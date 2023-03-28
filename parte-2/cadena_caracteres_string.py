# Tipo de dato compuesto string

nombre = 'Ismael Ortega'
email = "ismaelortega80@gmail.com"
direccion = '''Estado de México
México
55829
'''

print(type(nombre))
print(nombre)

# Mecanismos para componer, unir o crear cadenas de caracteres

# Concatenar sumando cadenas de caracteres
mensaje = 'Bienvenido(a), ' + nombre + '. Correo: ' + email
print(type(mensaje))
print(mensaje)

print()

# Interpolación de cadena de caracteres
mensaje = f'Bienvenido(a), {nombre}. Correo: {email}'
print(type(mensaje))
print(mensaje)

print()

# Utilizando format() de la clase str.
mensaje = f'Bienvenido(a), {nombre}. Correo: {email}'
print(type(mensaje))
print(mensaje)

print()

# Formato con %
mensaje = f'Bienvenido(a), %s. Correo: %s' % (nombre, email)
print(type(mensaje))
print(mensaje)

print()

#### Inmutabilidad de cadenas de caracteres (str):

lenguaje = 'Python'
print(lenguaje[0])
print(lenguaje[1])
print(lenguaje[2])
print(lenguaje[3])
print(lenguaje[4])
print(lenguaje[5])

# No se puede modificar un caracter de una variable de tipo string
# lenguaje[0] = 'p'   =>>> ERROR

# Alternativas
lenguaje = 'p' + lenguaje[1:]
print(lenguaje)

# Inmutables = se dice que son estáticos

print(id('python') == id('python'))

lenguaje = 'Python'.lower()   # Todos los metodos str entregan una copia de la cadena original, no modifican la cadena original
print(lenguaje)

#### Uso del método split()
valores = '2,3,5,7,11'
numeros = valores.split(',')
print(len(numeros))
print(numeros)
print(type(numeros))
print(type(numeros[0]))

print()

#### Uso del método find()
indice = valores.find('2')
print('El índice del elemento "2" es igual a: ', indice)
indice = valores.find('1')
print('El índice del elemento "1" es igual a: ', indice)
indice = valores.find('6')
print('El índice del elemento "6" es igual a: ', indice)  # -1 significa que no se encontro

print()

# Creación de una función (proceso) personalizado para buscar una cadena dentro de otra:

def encontrar(cadena,caracter):
    indice = -1
    for i in range(0,len(cadena)):
        if caracter == cadena[i]:
            indice = i
            break
    return indice

resultado = encontrar(valores, '2')
print('El índice del elemento "2" es igual a: ', resultado)

resultado = encontrar(valores, '7')
print('El índice del elemento "7" es igual a: ', resultado)

resultado = encontrar(valores, '8')
print('El índice del elemento "8" es igual a: ', resultado)

resultado = encontrar(valores, 1)  # Error si se pasa un int, debe de ser un caracter
print('El índice del elemento "1" es igual a: ', resultado)