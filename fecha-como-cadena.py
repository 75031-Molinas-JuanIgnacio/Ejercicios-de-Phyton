'''Desarrollar un programa que cargue por teclado una cadena de caracteres que se supone representa
una fecha en formato “dd/mm/aaaa”, y muestre por separado el día, el mes y el año. Ejemplo:
si la cadena ingresada es “16/03/2015” el programa debe mostrar: “Día: 16 - Mes: 03 - Año: 2016”.'''

'''El usuario ingresa la cadena de caracteres como se pide a continuacion'''
fecha = (input("Ingrese el dia/mes/año a continuacion:\t "))

'''Luego se procede a colocar la concatenacion de  indices a sus respectivas variables '''
dia = fecha[0] + fecha[1]
mes = fecha[3] + fecha[4]
año = fecha[6] + fecha[7] + fecha[8] + fecha[9]

'''Al final se muestran los resultados'''
print("Día:  ",dia, "\nMes:\t", mes, "\nAño:\t", año)

