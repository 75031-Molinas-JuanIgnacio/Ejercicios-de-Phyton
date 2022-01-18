'''Análisis de palabra'''

'''Se pide un programa que le solicite al usuario que ingrese una palabra. Con esa palabra calcular
los siguientes puntos:
    -Determinar la can􀆟dad de letras que tiene la palabra
    -Mostrar un mensaje que informe si la palabra termina en vocal '''

palabra  = input('Ingrese una palabra: ')
vocales = 'a','e','i','o','u'

'''Calculamos la cantidad de letras que tiene esa palabra y luego si esa palabra termina en vocal o no.'''

cantidad_letras = len(palabra)
print('La cantidad de letras que tiene esta palabra es de: ', cantidad_letras)


if palabra == vocales:
    print('La palabra que ingreso termino en vocal.')
else:
    print('La palabra que ingreso No termina en vocal.')