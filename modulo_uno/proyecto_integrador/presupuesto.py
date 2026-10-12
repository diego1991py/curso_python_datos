print("Presupuesto personal mensual")

nombre = input("Ingrese su nombre: ")
salario = float(input("Ingrese su salario mensual: "))

vivienda = float(input("Ingresar gastos de vivienda al mes: "))
alimentacion = float(input("Ingresar gastos de alimentacion al mes: "))
transporte = float(input("Ingresar gastos de transporte al mes: "))

total_gastos = vivienda + alimentacion + transporte
restante = salario - total_gastos

print("NOMBRE\tSALARIO\t\tGASTOS\t\tRESTANTE")
print(f"{nombre}\t${salario:,.2f}\t${total_gastos:,.2f}\t${restante:,.2f}")
