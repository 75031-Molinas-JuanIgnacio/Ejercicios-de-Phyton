'''Calculo de sueldo'''
'''Se conoce el monto del salario actual de un empleado, el nombre del empleado 
y el area funcional al cual pertenece. Se pide calcular el nuevo salario del empleado
sabiendo que obtuvo un incremento del 8% sobre su salario actual y un descuento de 2.5%
por servicios, informandos los resultados con el formato que se especifica a continuacion'''

'''Se pide los valores del empleado..'''
from platform import architecture


nombre = input('Ingrese su nombre: ')
area_funcional = input('Ingrese su area funcional a la cual pertenece por favor: ')
salario_actual = int(input('Ingrese su salario actual : '))

'''Calculando el nuevo salario...'''
incremento = (8 / 100) * salario_actual
print('El incremento sobre su salario',incremento)
descuento = (2.5 / 100)  * salario_actual
print('El descuento por sus servicios fue de : ',descuento)
nuevo_salario = (salario_actual + incremento) - descuento 
'''Se muestra a continuación lo que se pide'''
print('\n',nombre,'\n',area_funcional,'\n','Su saldo anterior era de :','\nSu nuevo saldo es de: ', nuevo_salario)