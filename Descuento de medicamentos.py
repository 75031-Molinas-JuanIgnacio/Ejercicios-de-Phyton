

print(" Medicamentos ")
medicamento =  "Paracetamol"
precio_medicamento = int(input(f"Ingrese el precio del {medicamento} "))
valor_descuento = 35
descuento_final =  (valor_descuento * precio_medicamento) // 100
monto_final = precio_medicamento - descuento_final 
print(f'El precio actual del {medicamento} es $ {precio_medicamento}. El monto de descuento es $ {descuento_final} . Y el monto final a pagar es $ {monto_final}')
