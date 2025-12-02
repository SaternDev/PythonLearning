# Vamos a crear una carpeta para un aula determinada, y dentro de esa carpeta, crearemos una carpeta para cada PC.

# Pide el nombre del aula (texto cualquiera) y un número de equipos M.

# Crea las carpetas: <AULA>/PC-01, <AULA>/PC-02 … <AULA>/PC-0M utilizando la librería pathlib.

# Usa un bucle for para generar los números de los PCs formateados con dos dígitos mediante la función zfill.

# Tanto si ya existe la carpeta como si no, debes indicarlo. En caso de que la carpeta no exista la creas.

# Librerías: from pathlib import Path

from pathlib import Path

currentDir = Path.cwd()

folder = Path(input('Dime el nombre de la carpeta para la aula: '))

if not folder.is_dir():
    print('La carpeta no Existe, se va a crear.')
    Path.mkdir(folder)
    
numEquip = int(input('Dime el número de equipos M: '))

for i in range (1,numEquip + 1):

    folderDir = Path(str(currentDir) + '/' + str(folder))
    folderCrea = Path(str(folder) + '/' + 'PC-' + str(i).zfill(2))

    if folderCrea.is_dir():
        print(f'Ya existe la carpeta: {str(folderCrea)} con lo cual no se va a crear')
    else:
        Path.mkdir(folderCrea)

print('Se han creado todas las carpetas adecuadas')