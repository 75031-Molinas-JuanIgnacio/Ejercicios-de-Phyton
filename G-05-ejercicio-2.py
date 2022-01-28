'''Operaciones de orden con tres números'''

'''Realizar un programa que tome tres números, los ordene de mayor a menor, y diga si el tercero es
el resto de la división de los dos primeros.'''
'''-----------------------------------------------------------------------------------'''
primer_numero = int(input('Ingrese el primer Número: '))
segundo_numero = int(input('Ingrese el segundo Número: '))
tercer_numero = int(input('Ingrese el tercer Número: '))

'''Para identificar el orden de los numeros ingresados'''

'''-----------------------------------------------------------------------------------'''
if (primer_numero > segundo_numero ) and  primer_numero > tercer_numero :
    mayor = primer_numero
    if segundo_numero > tercer_numero :
        mediano = segundo_numero
        menor = tercer_numero
    else:
        mediano = tercer_numero
        menor = segundo_numero
          
elif (segundo_numero > primer_numero) and segundo_numero > tercer_numero:
    mayor = segundo_numero
    if primer_numero > tercer_numero:
        mediano = primer_numero
        menor = tercer_numero
    else:
        mediano = tercer_numero
        menor = primer_numero

else:
    mayor = tercer_numero
    if primer_numero > segundo_numero:
        mediano = primer_numero
        menor = segundo_numero
    else:
        mediano = segundo_numero
        menor = primer_numero
'''-----------------------------------------------------------------------------------'''
'''Verificar si el tercer numero es el resto de la division de los Dos primeros.'''
print('El mayor numero es: ', mayor)
print('El segundo mayor es: ', mediano)
print('El menor número  es: ', menor)

resto = mayor % mediano
if menor ==  resto:
    print('El Tercer numero es  el resto de la Division de los Dos primeros.', resto)
else:
    print('El tercer numero NO es el resto de la division de los Dos primeros.', resto)




