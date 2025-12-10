# Recorre el directorio actual y muestra el archivo con fecha de modificación más reciente.
#  Para ello, investiga la función stat() que puedes aplicar sobre los archivos.

# Si no hay archivos, muestra “Sin archivos”.

# Librerías: from pathlib import Path

from pathlib import Path

# if Path.cwd().stat().st_size() == 0:
#     print('Sin archivos')

modTime = 0.
fileName = ''
hasFiles = False

for i in Path.cwd().iterdir():
    if i.is_file():   
        if not hasFiles:
            hasFiles = True

        modTimeFile = i.stat().st_mtime
        print(modTimeFile)
        if modTimeFile > modTime:
            modTime = modTimeFile
            fileName = str(i)
            
if hasFiles: 
    print(f'El archivo más reciente es: {fileName}')
else:
    print('Sin archivos')