# Recorre el directorio actual y suma el tamaño (en bytes) de todos los ficheros .log.

# Muestra la suma y, si es mayor o igual que 1 MB, imprime ALTO VOLUMEN, si no, imprime OK.

# Librerías: from pathlib import Path

from pathlib import Path

currentDir = Path.cwd()
tamaño = 0

for child in currentDir.iterdir():
    if child.is_file() and str(child.name).endswith('log'):
        tamaño += child.stat().st_size

if tamaño >= 1_048_576:
    print('ALTO VOLUMEN')
else:
    print('OK')