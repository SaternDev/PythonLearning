# Ejercicio 3: Pide al usuario 4 nombres de archivo o directorio.
# Usa la librería pathlib para determinar si existen y su tipo (fichero o directorio) y almacena esa información en un diccionario.
# Es decir, el diccionario debe contener para cada ruta si es archivo, directorio o si no existe.
# Muestra el contenido del diccionario recorriendo sus elementos.

from pathlib import Path

rutas = {

}

for _ in range(4):

    direct = Path(input('Dime el nombre del archivo o directorio: \n'))

    if direct.is_dir():
        rutas[str(direct)] = 'Directorio'
    elif direct.is_file():
        rutas[str(direct)] = 'Archivo'
    else:
        rutas[str(direct)] = 'No existe'

print(rutas)