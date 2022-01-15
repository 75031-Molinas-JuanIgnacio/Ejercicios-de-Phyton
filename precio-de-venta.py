''' Conociendo el precio de lista de un ar􀆡culo, determinar: '''
''' Precio de venta al contado (10 % de descuento) '''
''' Precio de venta con tarjeta (5 % de recargo \n '''

'''El usuario debera ingresar el precio del articulo que desea llevar '''
articulo = int(input("Ingrese el precio de lista del articulo")) 

descuento = 10
'''Proceso para calcular el descuento'''
calcular_descuento = (descuento * articulo) // 100

'''una vez sacado el descuento del articulo se procede a aplicarlo al mismo''' 
precio_de_venta_contado = articulo - calcular_descuento

'''En el proceso dle regargo pasa lo mismo qu lo anterior conla diferencia en que se suma al articulo ese interes del 5% '''

recargo = 5
calcular_regargo = (articulo * recargo) // 100
precio_con_tarjeta = articulo + calcular_regargo

'''A continuacion se muestra los resultados'''
print("Precio de venta de contado: \t ", precio_de_venta_contado," pesos ", "\n Precio de venta con tarjeta: \t",precio_con_tarjeta, " pesos ")

