# Lee users.txt y crea homes_check.txt que indique si la carpeta HOME de cada usuario existe (usa pathlib).
# El formato de cada línea debería ser: usuario -> home_path -> estado. El estado puede ser OK o No existe.

from pathlib import Path

diccionario = {

}

with open('users.txt', 'r') as f:
    for linea in f:
        clave, valor = linea.strip().split(',')
        diccionario[clave] = valor

with open('homes_check.txt', 'a') as l:
    for i in diccionario:
        directorio = Path(diccionario[i])
        if directorio.is_dir():
            l.write(f'{i} -> {str(directorio)} -> Ok\n')
        else:
            l.write(f'{i} -> {str(directorio)} -> No existe\n')