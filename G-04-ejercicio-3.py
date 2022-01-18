'''Calculo de Regularidad'''

'''La facultad pide un simple programa que pida las tres notas de un alumno en cualquier materia
y mostrar si el alumno esta libre, regular o promocionado. Las tres notas son los dos parciales mas la
nota de prác􀆟cos y las condiciones de regularidad están descriptas a con􀆟nuación:
* El promedio menor a 4 el alumno esta libre
* El promedio comprendido entre 4 y 8 el alumno esta regular
* El promedio mayor a 8 el alumno está promocionado. '''
'''Datos...'''
primera_nota = int(input('Ingrese la primera nota: '))
segunda_nota = int(input('Ingrese la segunda nota: '))
tercera_nota = int(input('Ingrese la tercera nota: '))

'''Proceso para calcular notas y promedio'''

suma_notas = primera_nota + segunda_nota + tercera_nota

promedio_notas = suma_notas // 3

'''Presentacion de resultados'''
if promedio_notas < 4 :
    print(' Usted quedo Libre.')
elif promedio_notas > 8 & promedio_notas < 4:
    print('Usted quedo Regular')
elif promedio_notas > 8:
    print('Usted esta Promocionado.')
else:
    print('Ingreso mal las notas')