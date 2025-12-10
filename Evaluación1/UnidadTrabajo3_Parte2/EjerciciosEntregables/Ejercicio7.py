# Pide al usuario un nombre de archivo hasta que exista en el directorio actual.

# Cuando exista, muestra su tamaño en bytes y termina el programa.

# Librerías: from pathlib import Path

from pathlib import Path

archivo = Path(input('Dime el nombre de un archivo: '))
tamañoArch = 0

while not archivo.is_file():
    print('El archivo no existe, dime un archivo que si exista')
    archivo = Path(input('Dime el nombre de un archivo: '))
else:
    tamañoArch = archivo.stat().st_size
    print(f'El archivo ocupa: {tamañoArch} bytes')