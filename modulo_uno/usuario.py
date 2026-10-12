print("Generador de nombres de usuario")

nombre = input("Ingresa su nombre: ").lower()
apellido = input("Ingresar su apellido: ").lower()
nacimiento = input("Ingresar su año de nacimiento: ")

usuario = nombre[0:3] + apellido[0:3] + nacimiento

print(f"El nombre de usuario creado es: {usuario}")