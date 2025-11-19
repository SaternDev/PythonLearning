# Pistas: librería sys y librería pathlib

# Pide como argumento un nombre de archivo y averigua su tamaño. Si su tamaño es >= 1 MB muestra “GRANDE”,
#  en caso contrario “PEQUEÑO”. (1 MB = 1_048_576 bytes)

# archivo.stat().stsize

import sys
import os

from pathlib import Path

if len(sys.argv) >= 2:
    #Serializamos la variable del nombre del archivo
    nomArchiv = Path(sys.argv[1])

    #Comprobamos que exista el archivo dado para no tener errores
    if Path.exists(nomArchiv):

        #El uso de almacenamiento
        storageUsing = os.path.getsize(nomArchiv)

        if storageUsing/1_048_576 >= 1:
            print('El archivo es grande')
        else:
            print('El archivo es pequeño')
    else:
        print('No existe el archivo')
else:
    print('No se ha dado ningún argumento')