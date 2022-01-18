'''Jornal de un Operario'''

'''Se necesita desarrollar un programa para el área de recursos humanos de una empresa que permita
informar el jornal de un determinado operario. Usted deberá cargar por teclado el código de turno
que el operario trabajó ese día (1- representa Diurno y 2- representa Nocturno) y la cantidad de horas
trabajadas.
La política de trabajo en la empresa es que los operarios de la misma pueden trabajar en el turno
diurno o nocturno. Si un operario trabaja en el turno nocturno el pago es 40.60 pesos la hora, si lo
hace en el turno diurno cobra 35.50 pesos la hora.'''
print('Ingrese el codigo de turno trabajado de la siguiente manera')
print('(1- representa Diurno y 2- representa Nocturno)')

'''Se les pide   datos al Usuario..'''
turno= int(input('Ingrese Su codigo: '))
horas = int(input('Ingrese la cantidad de horas que trabajó: '))

'''Calculo del sueldo por turno y horas y muestra del Resultado...'''
pago_diurno = 35.50 * horas
pago_nocturno = 40.60 *horas 
if turno == 1:
    print(' Su pago por haber trabajado estas',horas,
         'del turno de la mañana le corresponde: ', pago_diurno)
elif turno == 0:
    print(' Su pago por haber trabajado estas',horas,
         'del turno de la mañana le corresponde: ', pago_nocturno)
else:
    print('Ingreso mal los Datos.')