'''Duracion de vuelo'''
'''Desarrollar un programa que, cnociendo el horario de partida y de llegada de un vuelo(hora y minutos),
determine, ¿ cual es su duracion en minutos?. si el viajero necesita luego 45 min mas para ir del
 aeropuerto al hotel que ha reservado, ¿ A que hora llegara el mismo?'''

print ("Ingrese el horario de partida de la siguiente forma -> hh:mm , por ejemplo: 12:34 :  ")

horario_de_partida = input("Ingrese el horario de partida de la siguiente forma -> 12:34 : ")
horario_de_llegada = input("Ingrese el horario de llegada ")
'''Procesos'''
'''Saco la hora de partida y la convierto a numero entero'''

hora_partida = int(horario_de_partida[0] + horario_de_partida[1])
'Ahora los minutos los transformo en enteros'
minutos_partida = int(horario_de_partida[3] + horario_de_partida[4])

'''Sacamos la hora de llegada y aplico lo mismo'''
hora_llegada = int(horario_de_llegada[0] + horario_de_llegada[1])

'''Y continuo igual con los minutos'''
minutos_llegada = int(horario_de_llegada[3] + horario_de_llegada[4])

'''Hacemos el pasaje de esas horas ingresadas a minutos y lo acumulo 
minutos tanto la partida como la llegada'''

minutos_partida = minutos_partida + (hora_partida * 60)
minutos_llegada = minutos_llegada + (hora_llegada * 60)
''' Variable de tiempo demorado son 45 minutos'''
tiempo_demorado = 45
'''Duracion del Viaje'''

hora_llegada_al_hotel = (minutos_llegada + tiempo_demorado)//60
print(hora_llegada_al_hotel)
minutos_llegada_al_hotel = (minutos_llegada + tiempo_demorado)%60
print(minutos_llegada_al_hotel)
duracion_viaje_minutos = minutos_llegada - minutos_partida
'''Se muestran los resultados obtenidos: '''

print("La duracion del viaje es :  ", duracion_viaje_minutos, "minutos")
print("Llega a las : ", (str(hora_llegada_al_hotel) + ":" + str(minutos_llegada_al_hotel)))