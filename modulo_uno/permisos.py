print("Cadena de permisos en Linux")

diccionario = {
    "0": "---",
    "1": "--x",
    "2": "-w-",
    "3": "-wx",
    "4": "r--",
    "5": "r-x",
    "6": "rw-",
    "7": "rwx"
}

codigo = input("Ingresar cadena de caracteres de 3 digitos: ")

resultado = str(diccionario[codigo[0]] + diccionario[codigo[1]] + diccionario[codigo[2]])

print(resultado)
