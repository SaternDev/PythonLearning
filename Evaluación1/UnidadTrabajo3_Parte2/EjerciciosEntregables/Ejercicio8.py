# Muestra un menú en bucle con opciones:

# 1) Listar archivos del directorio actual 2) Crear carpeta ‘logs’ 3) Salir

# Usa while True y condicionales para implementar cada una de las opciones.

# Librerías: from pathlib import Path

from pathlib import Path

currentDir = Path.cwd()

while True:
    print('Elige lo que quieras realizar: ')
    print('# 1) Listar archivos del directorio actual 2) Crear carpeta "logs" 3) Salir')

    eleccionPlay = int(input('Escribe el número de la opción que quieras: '))

    if eleccionPlay == 1:
        for i in currentDir.iterdir():
            print(i)

    elif eleccionPlay == 2:
        folderName = Path(input('Dime el nombre de la carpeta que quieres crear: '))

        while folderName.is_dir():
            print('Ya existe esa carpeta.')
            folderName = Path(input('Dime otro nombre de carpeta: '))
        else:
            Path.mkdir(folderName)
            print('Se ha creado la carpeta')

    elif eleccionPlay == 3:
        break