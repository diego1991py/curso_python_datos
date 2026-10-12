import random

print("ALERTA DE TEMPERATURA")

estado = 1

while True:
    temperatura = random.randint(0, 100)
    if temperatura < 75:
        print(f"Temperatura: {temperatura}°C")
        print("Continuar programa")
        print("Ingrese 1 para continuar, 0 para parar")
        estado = int(input("Ingresar opción: 1, 0: "))
        if estado == 1:
            print("------")
            #temperatura = random.randint(0, 100)
        elif estado == 0:
            print("Fin del programa")
            break
        else:
            print("Opción no valida")
    else:
        print(f"Temperatura fuera del rango: {temperatura}°C")
        break