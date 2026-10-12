print("Convertidor de tiempo")

segundos = int(input("Ingresar cantidad en segundos: "))

minutos = segundos // 60

segundos = segundos % 60

horas = minutos // 60

minutos = minutos % 60

dias = horas // 24

horas = horas % 24


print(f"{dias} días, {horas} hh, {minutos} mm, {segundos} ss")