# Pide al usuario un nombre de usuario (por ejemplo rafa) y 
# guarda en users.txt el nombre y su ruta HOME estimada (en Linux /home/<usuario>) usando pathlib.
# El formato de cada línea debería ser: nombre,ruta. Si el usuario ya estaba, no lo repitas.
from pathlib import Path

name = input('Dime el nombre de usuario: ')
namein = False

if Path('users.txt').exists():
    with open('users.txt', 'r') as l:
        for linea in l:
            clave, valor = linea.strip().split(',')
            if clave == name:
                namein = True

with open('users.txt', 'a') as f:
    if not namein:
        f.write(f'{name}, /home/{name}\n')
    else:
        print('El nombre ya está')