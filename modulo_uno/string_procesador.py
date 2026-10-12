print("Procesador de nombres para archivos")

nombre = input("Ingresar nombre del archivo: ")

nuevo_nombre = nombre.replace(" ", "_").lower()

print(f"El nombre: {nombre} fue reemplazado por: {nuevo_nombre}")

