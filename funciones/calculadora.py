# Esto es una operación aritmética sencilla
# print(4 + 5)
# a = float(input('Ingrese el primer número: '))
# b = float(input('Ingrese el segundo número: '))
# print(a + b)

# Realizamos la misma operación creando un método
# Para crear un método usamos la palabra reservada DEF (definir)
# Luego ponemos el nombre del método
# Finalmente definimos los argumentos del métodos, es decir, 
# los insumos que necesitará la función para trabajar
print('\nOperaciones aritméticas con 2 números mediante métodos')
def suma(a,b):
    resultado = a + b
    print(f'{a} + {b} = {resultado}')

def resta(a,b):
    resultado = a - b
    print(f'{a} - {b} = {resultado}')

def multiplicacion(a,b):
    resultado = a * b
    print(f'{a} x {b} = {resultado}')

def division(a,b):
    try:
        resultado = a / b
        print(f'{a} / {b} = {resultado}')
    except ZeroDivisionError:
        print('No se puede dividir por 0.')
    except Exception as error:
        print(f'No se puede dividir por el siguiente error: {error}')

def convertir_float(valor):
    try:
        resultado = float(valor)
        return resultado
    except ValueError: 
            print('No se puede convertir el valor ingresado a decimal')
    except Exception as error:
        print(f'No se puede realizar la conversión por el siguiente error: {error}')

numero1 = convertir_float(input('Ingrese el primer número: '))
numero2 = convertir_float(input('Ingrese el segundo número: '))

suma(numero1,numero2)
resta(numero1,numero2)
multiplicacion(numero1,numero2)
division(numero1,numero2)