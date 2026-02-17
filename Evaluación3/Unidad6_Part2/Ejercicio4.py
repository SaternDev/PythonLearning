# Crea paths.txt con varias rutas (una por línea).
# Luego lee el fichero y crea paths_status.txt indicando para cada ruta si existe y si es archivo o directorio (usa pathlib).
# En concreto, los estados pueden ser: Directorio, Archivo, Otro, No Existe.
# El formato de cada línea debería ser: ruta -> estado

from pathlib import Path

directorios = []
archivos = []
otro = []
noExiste = []

with open('paths.txt', 'r') as f:
    if Path(f.readline).exists():
        pass