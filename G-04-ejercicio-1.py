'''Suma Division y Potencia'''
'''Se necesita desarrollar un programa que permita calcular la suma
de 3 numeros.si el resultado es mayor a 10 dividir por 2 (mostrar su 
resultado sin decimales), en caso contrario elevar el resultado al cubo'''

numero_1 = int(input('Ingrese el primer numero: '))
numero_2 = int(input('Ingrese el segundo numero: '))
numero_3 = int(input('Ingrese el tercer numero: '))
suma = numero_1 + numero_2 + numero_3
print('ToTal de la suma: ', suma)
'''Proceso..'''

if suma > 10:
    resultado = suma // 2
else:
    resultado = suma ** 3
print('Resultado:', resultado)