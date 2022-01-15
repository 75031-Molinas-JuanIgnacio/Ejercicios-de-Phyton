'''Desarrollar un programa que cargue por teclado un importe (can􀆟dad de dinero) expresado como
número en coma flotante y muestre un mensaje con esa can􀆟dad pero en dos formatos: en uno debe
aparecer precedida por el signo “$” y en el otro debe aparecer precedida por la palabra “pesos”.'''
'''EL usuario ingresa lo que se le pide a continuacion: '''

importe = float(input("Coloque la cantidad de dinero: "))
'''Se muestra  las 2 formas que pide el Usuario en un solo print'''
print("PRIMERA FORMA\n","La canrtidade de dinero ingresada es de: ", importe, "$","\nSEGUNDA FORMA\n","\n La cantidad de denero ingresada esa de: ", importe, "pesos")