# Un  técnico  necesita  comprobar  si  una  ruta  de instalación  existe  en  el  sistema.
# El programa debe recibir la ruta como argumento.
# Un ejemplo de ruta sería: /usr/bin. 
# Si la ruta no existe, debe mostrar un mensaje indicando que “falta la instalación”. 
# Si existe y es una carpeta, mostrará que “la instalación es válida”.
# Si existe, pero es un archivo, mostrará que la ruta “no es válida para instalación”.

#Un programa debe recibir como argumento una ruta, la qual va a tener que ser buscada por el sistema.
#en el caso de que el directorio exista, imprimirá "la instalacion es válida", en caso contrario,
#"falta la instalación". En caso de ser un archivo, muestra "no es válida la instalación"


#Necesitaremos una variable que almacena la ruta.

import sys
from pathlib import Path

#Comprobamos que se haya dado algún valor
if len(sys.argv) >= 2:
    print('Si se ha dado argumento')
    route = Path(sys.argv[1])
    
    if route.exists():
        print('La instalación es válida')
        if route.is_dir():
            print('INSTALACION VALIDA')
        elif route.is_file():
            print('RUTA INVALIDA PARA INSTALACION')
        else:
            print('Tipo de recurso no soportado')
    else:
        print('Falta la instalación')
else:
    print('No se ha dado argumento')