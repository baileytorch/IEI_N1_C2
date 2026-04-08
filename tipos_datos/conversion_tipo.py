nombre_personal = input('Ingrese su nombre: ')
saludo = 'Buen día '
print(type(nombre_personal))
print(nombre_personal)

# CONCATENACIÓN de cadenas de texto
print(saludo + nombre_personal)

str_numero_entero = input('Ingrese un número entero: ')
numero_entero = int(str_numero_entero)
numero_decimal = float(str_numero_entero)
print(type(numero_entero))
print(type(numero_decimal))
print(numero_entero)
print(numero_decimal)

numero_uno = 25
numero_dos = 50

# La operacion + con 2 números, opera aritméticamente sumándolos y entregando el resultado
print(numero_uno + numero_dos)
# La operacion + con 2 cadenas de texto, opera semánticamente concatenándolos y entregando el string resultante
print(saludo + str_numero_entero)
# La operación + con 2 tipos de datos distintos arroja ERROR
# print(str_numero_entero + numero_dos)

# Solicite al usuario que ingrese su nombre y edad y muéstrelos por pantalla con un saludo.