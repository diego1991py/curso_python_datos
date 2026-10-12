print("Calculadora de Espacio en Disco")

megabytes = float(input("Ingresar espacio en Megabytes: "))

gigabytes = megabytes / 1000

terabytes = gigabytes / 1000

print(f"{megabytes} Megabytes corresponden a:\n{gigabytes} Gigabytes\n{terabytes} Terabytes")