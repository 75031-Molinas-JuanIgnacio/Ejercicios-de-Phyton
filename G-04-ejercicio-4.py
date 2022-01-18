'''Punto en el plano'''

'''Se pide realizar un programa que ingresando el valor x e 
y de un punto determine a que cuadrante
pertenece en el sistemas de coordenadas '''

variable_x = int(input('Ingrese el valor de la variable X: '))
variable_y = int(input('Ingrese el valor de la variable y: '))

primer_cuadrante = variable_x >= 0 & variable_y >=0
segundo_cuadrante = variable_x <= -1 & variable_y >= 0
tercer_cuadrante = variable_x <=0 -1 & variable_y <= -1
cuarto_cuadrante = variable_x >= 0 & variable_y <= -1

if primer_cuadrante:
    print('El punto esta en el primer cuadrante.')
elif segundo_cuadrante:
    print('El punto esta en el segundo cuadrante.')
elif tercer_cuadrante:
    print('El punto esta en el tercer cuadrante.')
else:
    print('El punto esta en el cuarto cuadrante.')
 