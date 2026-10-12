print("Estadistica de Uso de CPU y Memoria RAM")


memoria_uno = float(input("Ingresar consumo de memoria de programa 1 en %: "))
cpu_uno = float(input("Ingresar uso de CPU de programa 1 en %: "))

memoria_dos = float(input("Ingresar consumo de memoria de promama 2: "))
cpu_dos = float(input("Ingresar uso de CPU de programa 2 en %: "))

memoria_tres = float(input("Ingresar consumo de memoria de programa 3: "))
cpu_tres = float(input("Ingresar uso de CPU de programa 3 en %: "))

memoria_cuatro = float(input("Ingresar consumo de memoria de programa 4: "))
cpu_cuatro = float(input("Ingresar uso de CPU de programa 4 en %: "))

memoria_cinco = float(input("Ingresar consumo de memoria de programa 5: "))
cpu_cinco = float(input("Ingresar uso de CPUde programa 5 en %: "))


promedio_ram = (memoria_uno + memoria_dos + memoria_tres + memoria_cuatro + memoria_cinco) / 5
promedio_cpu = (cpu_uno + cpu_dos + cpu_tres + cpu_cuatro + cpu_cinco) / 5

print(f"El promedio de uso de la Memoria es: {promedio_ram:.2f} %")

print(f"El promedio de uso de la CPU es: {promedio_cpu:.2f} %")