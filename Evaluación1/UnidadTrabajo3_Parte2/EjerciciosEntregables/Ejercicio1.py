# Recorre el directorio actual y cuenta cuántos archivos terminan en .log.

# Muestra el total encontrado.

# Librerías: from pathlib import Path

from pathlib import Path

currentDir = Path.cwd()
count = 0

for child in currentDir.iterdir():
    if child.is_file() and str(child.name).endswith('log'):
        count += 1

print(f'Hay {count} archivos que terminan por .log')