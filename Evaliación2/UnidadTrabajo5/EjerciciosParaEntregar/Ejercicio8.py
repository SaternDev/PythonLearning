# Ejercicio 8: Vamos a realizar un análisis de las siguientes rutas críticas del sistema:

# Guarda en un diccionario si cada una existe y si es un archivo, un directorio o no existe.
# Muestra un informe con el sistema operativo, número de CPUs, fecha actual y el estado de cada ruta.
# Usa las librerías pathlib, platform, os y datetime.

from pathlib import Path

import platform
import os

from datetime import datetime

rutas = ["/", "/home", "/var", "/tmp", "/usr", "/bin", "/opt", "/noexiste"]

routeDic = {

}

for i in range(len(rutas)):
    i = Path(rutas[i])

    if i.exists():

        if i.is_dir():
            routeDic[str(i)] = 'Existe y es un directorio'

        elif i.is_file():
            routeDic[str(i)] = 'Existe y es un archivo'

    else:
        routeDic[str(i)] = 'No Existe'

print(routeDic)
for j in routeDic:
    print(f'El estado de la ruta {j} es: {routeDic[j]}')
print(f'El sistema operativo es {platform.system()}, el numero de CPUs es {os.cpu_count()}, la fecha es {datetime.now().date()} y la hora es {datetime.now().time()}')