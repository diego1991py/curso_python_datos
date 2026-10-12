import os

print("Variables de Entorno Linux")

usuario = os.getenv("USER")
home = os.getenv("HOME")
directorio = os.getcwd()
lenguaje = os.getenv("LANG")


print(f"USUARIO: {usuario}")
print(f"HOME: {home}")
print(f"DIRECTORIO: {directorio}")
print(f"IDIOMA: {lenguaje}")