'''Impuesto Automotor'''

'''Crear un programa que permita calcular los impuestos que 
debe pagar un auto conociendo su modelo (año de fabricacion)
y tipo (P: particular, T:taxi, R:remis) Para calcular los impuestos
tener en cuenta que:
  
    *Los autos particulares de menos de 10 años de antigüedad pagan $200,
     entre 10 y 20 años pagan $150 y no pagan impuestos los que tenen más de 20 años.
    *Los taxis pagan impuestos como auto par􀆟cular, más $150 por la licencia de taxi.
    *Los remises pagan $100 por cada año de an􀆟güedad de su vehículo'''

'''Se piden  que ingresen los datos al usuario'''
modelo_del_auto = int(input('Ingrese el modelo de su auto ( Año ):  '))
tipo_auto = input('indique con mayuscula el tipo de auto (P: particular, T:taxi, R:remis): ')
licencia_taxi = 150

''' Se Calcula el Impuesto Correspondiente..'''
if tipo_auto == 'P':
    if   modelo_del_auto < 10 :
        impuesto_por_antiguedad = modelo_del_auto + 200
    elif modelo_del_auto == modelo_del_auto > 10 & modelo_del_auto < 20 :
        impuesto_por_antiguedad = modelo_del_auto + 150
    else:
        impuesto_por_antiguedad = print('Usted no paga impuesto por tener mas de 20 años de Antiguedad.')

        '''*Los taxis pagan impuestos como auto par􀆟cular, más $150 por la licencia de taxi.'''
elif tipo_auto== 'T':
    if modelo_del_auto < 10 :
        impuesto_por_antiguedad = modelo_del_auto + 200 
        print('El impuesto que paga por tener menos de 10 años de antiguedad es: ', 
              impuesto_por_antiguedad, 'pesos')
        '''Se suma  los años de antiguedad mas la licencia de taxi'''     
        total_a_pagar = impuesto_por_antiguedad + licencia_taxi
        print(' El total a pagar es de: ',total_a_pagar)

    elif modelo_del_auto == modelo_del_auto > 10 & modelo_del_auto < 20  :
        impuesto_por_antiguedad = modelo_del_auto + 150
        print('El impuesto que paga por tener entre 10 años y 20 de antiguedad es: ', 
              impuesto_por_antiguedad, 'pesos')
        '''Se suma  los años de antiguedad mas la licencia de taxi'''
        total_a_pagar = impuesto_por_antiguedad + licencia_taxi
        print(' El total a pagar es de: ',total_a_pagar)
    else:
        impuesto_por_antiguedad = print('Usted no paga impuesto por tener mas de 20 años de Antiguedad.')

    '''*Los remises pagan $100 por cada año de an􀆟güedad de su vehículo'''
elif tipo_auto== 'R':
    suma_años = 0
    if modelo_del_auto < 10 :
            impuesto_por_antiguedad = modelo_del_auto * 100
            print('El impuesto que paga por tener menos de 10 años de antiguedad es: ', 
              impuesto_por_antiguedad, 'pesos')
        

    elif modelo_del_auto == modelo_del_auto > 10 & modelo_del_auto < 20 :
        impuesto_por_antiguedad = modelo_del_auto * 100
        print('El impuesto que paga por tener entre 10 años y 20 de antiguedad es: ', 
              impuesto_por_antiguedad, 'pesos')
        
    else:
        impuesto_por_antiguedad = print('Usted no paga impuesto por tener mas de 20 años de Antiguedad.')

        print('No se calculo ningun impuesto por que no puso los datos correctamente.')

        '''Se muestran los resultados'''
print('El modelo del auto es: ', modelo_del_auto, 'y su impuesto es de: ', impuesto_por_antiguedad , 'pesos')

