from math import pow
print("Calculadora de IMC")

nombre = input("Ingresar nombre: ")

edad = input("Ingrear edad: ")

peso = float(input("Ingresar peso en Kg: "))

estatura = float(input("Ingresar estatura en metros: "))

imc = (peso/pow(estatura, 2))

print(f"nombre\tedad\tIMC")
print(f"{nombre}\t{edad}\t{imc:.2f}")