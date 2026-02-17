# Pide al usuario un nombre de usuario (por ejemplo rafa) y 
# guarda en users.txt el nombre y su ruta HOME estimada (en Linux /home/<usuario>) usando pathlib.
# El formato de cada línea debería ser: nombre,ruta. Si el usuario ya estaba, no lo repitas.

name = input('Dime el nombre de usuario: ')
namein = False

with open('users.txt', 'r') as l:
    if name not in l:
        namein = True

with open('users.txt', 'a') as f:
    if not namein:
        