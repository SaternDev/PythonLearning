# Pistas: librería pathlib, librería os

# Obtén el directorio actual con la clase Path de la librería pathlib e imprímelo por pantalla. Obtén su contenido con la función listdir 
# de la librería os e imprime por pantalla. A continuación, comprueba si existe la carpeta “logs” en el directorio actual.
#  Para ello, monta tú mismo la ruta para que sea de tipo Path.

# Si no existe, créala y muestra “Carpeta creada”.
# Si existe, muestra “Carpeta ya existe”.

from pathlib import Path
import os

#Comprobamos el directorio en el que estamos
actual = Path.cwd()
print(f'El directorio actual es: {actual}')

#Listamos el contenido del directorio actual
actualDir = os.listdir(actual)
print(f'Este es el contenido del directorio actual: {actualDir}')

#Comprobamos si existe la carpeta "logs" en el directorio que estamos
newFolder = actual/"logs"
if (newFolder.exists()):
    print('Existe el directorio "logs."')
else:
    #Crea el directorio si no se encuentra
    print('No existe el directorio "logs" con lo cual se va a crear.')
    newFolder.mkdir()