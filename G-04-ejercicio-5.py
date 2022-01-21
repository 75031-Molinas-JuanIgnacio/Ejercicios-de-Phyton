'''Postulantes a un empleo'''

'''Se tienen los datos de tres postulantes a un empleo, a los que se les realizó un test de capacitación.
Por cada postulante, se tiene entonces la siguiente información: nombre del postulante, can􀆟dad total
de preguntas que se le realizaron y can􀆟dad de preguntas que contestó correctamente.

Se pide confeccionar un programa que lea los datos de los tres postulantes, 
    -informe el nivel de cada uno según los criterios de aprobación que se indican mas abajo,
     e indique finalmente el nombre del postulante que ganó el puesto.
    Los criterios de aprobación son los siguientes, en función del porcentaje
de respuestas correctas sobre el total de preguntas realizadas a cada postulante:
    
    -Nivel Superior: Porcentaje 90 %
    -Nivel Medio: 75 % <= Porcentaje < 90 %
    -Nivel Regular: 50 % <= 6 Porcentaje < 75 %
    -Fuera de Nivel: Porcentaje < 50 % '''
    
'''Datos de los postulantes..'''
nombre1 = input('Porfavor ingrese su nombre: ')
cant_preguntas1 = int(input('Ingrese la cantidad de preguntas que  se le realizaron: '))
cant_respuestas1 = int(input('Ingrese la cantidad de preguntas correctas que contestó: '))

nombre2 = input('Porfavor ingrese su nombre: ')
cant_preguntas2 = int(input('Ingrese la canatidad de preguntas que  se le realizaron: '))
cant_respuestas2 = int(input('Ingrese la cantidad de preguntas correctas que contestó: '))

nombre3 = input('Porfavor ingrese su nombre: ')
cant_preguntas3 = int(input('Ingrese la cantidad de preguntas que  se le realizaron: '))
cant_respuestas3 = int(input('Ingrese la cantidad de preguntas correctas que contestó: '))

'''Calcular los datos de los postulantes e informar los criterios de aprobacion''' 

porcentaje1 = cant_respuestas1 / cant_preguntas1 * 100
porcentaje2 = cant_respuestas2 / cant_preguntas2 * 100
porcentaje3 = cant_respuestas3 / cant_preguntas3 * 100

'''Con los resultados de los porcentaje se compara el nivel del Postulante'''

if porcentaje1 > 90:
    nivel1 = 'Nivel Superior'
elif 75 <= porcentaje1 < 90:
    nivel1 = 'Nivel Medio'
elif 50 <= porcentaje1 < 75:
    nivel1 = 'Nivel Regular'
else:
    nivel1 = 'Fuera de Lugar'

if porcentaje2 > 90:
    nivel2 = 'Nivel Superior'
elif 75 <= porcentaje2 < 90:
    nivel2 = 'Nivel Medio'
elif 50 <= porcentaje2 < 75:
    nivel2 = 'Nivel Regular'
else:
    nivel2 = 'Fuera de Lugar'

if porcentaje3 > 90:
    nivel3 = 'Nivel Superior'
elif 75 <= porcentaje3 < 90:
    nivel3 = 'Nivel Medio'
elif 50 <= porcentaje3 < 75:
    nivel3 = 'Nivel Regular'
else:
    nivel3 = 'Fuera de Lugar'

'''Ordenamiento de los Postulantes '''

if (porcentaje1 > porcentaje2) and porcentaje1 > porcentaje3: 
    mayor_nombre = nombre1
    mayor_nivel = nivel1
    mayor_porcentaje = porcentaje1
elif porcentaje2 > porcentaje3:
    mayor_nombre = nombre2
    mayor_nivel = nivel2
    mayor_porcentaje = porcentaje2
else:
    mayor_nombre = nombre3
    mayor_nivel = nivel3
    mayor_porcentaje = porcentaje3

'''Se muestran los resultados de los Postulantes'''

print('La persona que ganó el Puesto fue: ',mayor_nombre,
'contestando el ', mayor_porcentaje,'%','\t correctamente ',' obteniendo asi el ', mayor_nivel)
