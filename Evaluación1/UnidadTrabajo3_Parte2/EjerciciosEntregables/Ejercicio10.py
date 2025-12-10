# Pide por teclado nombres de archivos de backup hasta que el usuario introduzca FIN.

# Cuenta cuántos terminan en .zip y cuántos en .tar.gz o .tgz y muéstralo al final. Cuenta también los archivos introducidos
#  con cualquier otra extensión.

# Librerías: from pathlib import Path

from pathlib import Path

countZip = 0
countTar = 0
countGZ = 0
countTGZ = 0
countOthers = 0

fileNames = Path(input('Dime el nombre de un archivo de backup (Escribe FIN en caso de querer termianr el programa): '))

while str(fileNames) != 'FIN':
    if fileNames.exists():
        if fileNames.is_file():
            if str(fileNames.suffix) == '.zip':
                countZip += 1

            elif str(fileNames.suffix) == '.tar':
                countTar += 1

            elif str(fileNames.suffix) == '.gz':
                countGz += 1

            elif str(fileNames.suffix) == '.tgz':
                countTGZ += 1

            else:
                countOthers += 1

        elif fileNames.is_dir():
            print('Es un directorio')
    else:
        print('El archivo no existe')

    fileNames = Path(input('Dime el nombre de un archivo de backup (Escribe FIN en caso de querer termianr el programa): '))
else:
    print(f'Hay un total de {countZip} archivos terminados en "zip", {countTar} terminados en "tar", {countGZ} terminados en "GZ", {countTGZ} terminados en "TGZ" y {countOthers} archivos terminados en cualquier otra terminologia')