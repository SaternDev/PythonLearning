# Pide un número N por teclado y crea carpetas backup_1 … backup_N en el directorio actual.

# Si alguna ya existe, no pasa nada. Indica para cada carpeta si la creas o si ya existía.

# Librerías: from pathlib import Path

from pathlib import Path

folderNum = input('Dime un número para crear la carpera (No se peuden decimales ni menores a 0): \n')

folder = 'backup_' + folderNum

while int(folderNum) < 0:
    print('Has escrito un número inadecuado')
    folderNum = input('Dime un número para crear la carpera (No se peuden decimales ni menores a 0): \n')

if Path.is_dir(Path(folder)):
    print('Existe la carpeta')
else:
    print('No existe la carpeta, la voy a crear')
    Path.mkdir(Path(folder))