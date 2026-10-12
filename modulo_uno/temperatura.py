print("Conversor de temperatura")

celcius = float(input("Ingresar temperatura en grados Celcius: "))

fahrenheit = (celcius  * 9 / 5 ) + 32
kelvin = celcius + 273.15

print(f"la temperatura de {celcius}° Celcius es de:\n{fahrenheit}°F\n{kelvin}°K")