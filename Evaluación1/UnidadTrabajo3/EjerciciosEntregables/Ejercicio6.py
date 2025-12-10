# En el directorio actual, si NO existe un fichero llamado “config.ini”, copia el fichero “config.example.ini” a “config.ini”.
# Deberás comprobar también que el fichero “config.example.ini” exista, si no, muestra el mensaje “Falta el archivo de ejemplo”.
# Si ya existe “config.ini”, muestra el mensaje “Config existente”.En el directorio actual, si NO existe un fichero llamado “config.ini”,
# copia el fichero “config.example.ini” a “config.ini”. Deberás comprobar también que el fichero “config.example.ini” exista, si no,
# muestra el mensaje “Falta el archivo de ejemplo”.
# Si ya existe “config.ini”, muestra el mensaje “Config existente”.

from pathlib import Path
import shutil

actual = Path.cwd()
configDoc = actual/"config.ini"
ficheroEjem = actual/"configExample.ini"

if configDoc.exists():
    print('Existe')
else:
    print('No Existe')
    if ficheroEjem.exists():
        print('Existe Fichero ejemplo')
        shutil.copy(ficheroEjem, configDoc)
    else:
        print('No existe Fichero Ejemplo')