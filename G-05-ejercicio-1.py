import random
'''Tirada de moneda'''

'''Programar una tirada de una moneda (opciones: cara o cruz) aleatoriamente. 
Permitir que un jugador apueste a cara o cruz y luego informar si acertó o no con su apuesta.'''
moneda = int(input('Ingrese su apuesta (1) para Cara y (0) para Cruz: '))

apuesta = random.randint(0,1)
print(apuesta)
if apuesta == 1 & moneda == 1 :
    print('Su apuesta fue: ',apuesta,' por lo tanto usted ')
    print('Acerto con exito, usted ganó, Felicitaciones!! :)')
elif apuesta == 0 & moneda == 0:
    print('Su apuesta fue: ',apuesta,' por lo tanto usted ')
    print('FELICITACIONES, ha acertado con Exito!! :) :)')
else:
    print('Su apuesta fue: ',apuesta,' por lo tanto usted ')
    print('Lamentablemente perdió, lo siento! :( ')
    
