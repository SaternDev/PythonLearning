# Recorre el directorio actual y muestra el archivo con fecha de modificación más reciente. Para ello, investiga la función stat() que puedes aplicar sobre los archivos.

# Si no hay archivos, muestra “Sin archivos”.

# Librerías: from pathlib import Path

from pathlib import Path

if Path.cwd().stat().st_size() == 0:
    print('Sin archivos')

for i in Path.cwd().iterdir():
    print(i.stat())
    print(i)