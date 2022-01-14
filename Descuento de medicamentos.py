'''Calcular el descuento y el monto a pagar por un medicamento cualquiera en una farmacia (cargar
por teclado el precio de ese medicamento) sabiendo que todos los medicamentos 􀆟enen un descuento
del 35 %.
Mostrar el precio actual, el monto del descuento y el monto final a pagar. '''
print("  Descuento de Medicamentos ")

''' En la llinea siguiente el Usuario tendria que cargar el precio del medicamento que desee al cual quiere que se le aplique el descuento'''
medicamento = int(input("Ingrese el precio del medicamento"))

'''Se aplica el Descuento'''
descuento =  (35 * medicamento) //100

'Se le aplica el descuento al monto inicial que ingreso el usuario'
monto_final = medicamento - descuento

'''Luego se muestra el resultado''' 
print("El precio actual del Medicamento ingresado ", medicamento, " $ pesos ", " El monto del descuento es de ", descuento, " $ pesos", "Y el monto final a pagar es de ", monto_final, " $ pesos " )