salario_bruto = float(input("Salario bruto del empleado: "))
camisas_vendidas = int(input("Cantidad de camisas vendidas: "))
precio_por_camisa = float(input("Precio de cada camisa: "))

seguro_salud = salario_bruto * 0.08
impuesto_renta = salario_bruto * 0.12

total_ventas = camisas_vendidas * precio_por_camisa
regalias = total_ventas * 0.03

salario_neto = salario_bruto - seguro_salud - impuesto_renta + regalias

print(f"Salario neto: {salario_neto:.2f} unidades monetarias")