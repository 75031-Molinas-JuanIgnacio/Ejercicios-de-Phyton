'''Control elctoral'''

'''Desarrollar un programa de control electoral en un centro vecinal, en el que se ingresen,
para cierto candidato: apellido, nombre y cantidad de votos. Luego presentar en pantalla
un resumen que muestre: iniciales del candidato, cantidad de votos entre parentesis, y
debajo  una línea con tantas "x" como votos obtenidos(por ejemplo, el candidato obtuvo 4 votos
, debera aparecer una linea como esta:"xxxx" con 4 letras "x") (Asumimos que en el centro
vecinal no hay demasiado electores, de forma que podamos estar seguros que no habra mile o
millones de votos... solo unos pocos para darle sentido).'''

'''Se ingresan los datos..'''
nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
cantidad_votos =  int(input('Ingrese  la cantidad de votos : '))

if cantidad_votos == 1:
    cantidad_de_votos_obtenidos = 'x'
elif cantidad_votos == 2:
    cantidad_de_votos_obtenidos = 'xx'
elif cantidad_votos == 3:
    cantidad_de_votos_obtenidos = 'xxx'
elif cantidad_votos == 4:
    cantidad_de_votos_obtenidos = 'xxxx'
elif cantidad_votos == 5:
    cantidad_de_votos_obtenidos = 'xxxxx'
elif cantidad_votos == 6:
    cantidad_de_votos_obtenidos = 'xxxxxx'
else:
    cantidad_de_votos_obtenidos = print('No hubieron votos.')

'''Se presentan los datos'''
print('Sus iniciales son: ', nombre[0] + apellido[0], ' \n  La cantidad de votos fue de : ',
    '(',cantidad_votos,')','\n',cantidad_de_votos_obtenidos)


