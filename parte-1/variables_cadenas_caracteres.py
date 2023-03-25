# Asignar en una variable una literal de cadena de caracteres
nombre = 'Ismael'
apellido = "Ortega"
nombre_completo = nombre + ' ' + apellido

print('Nombre:', nombre)
print('Apellido:', apellido)
print('Nombre completo:', nombre_completo)

print('Tipo de dato de la variable nombre:', type(nombre))
print('Tipo de dato de la variable apellido:', type(apellido))
print('Tipo de dato de la variable nombre_completo:', type(nombre_completo))

edad = 23

informacion = nombre_completo + ' tiene ' + str(edad) + ' años.'

print(informacion)

# Mejorando la sentencia anterios

informacion = '{} tiene {} años.'.format(nombre_completo, edad)

print(informacion)
