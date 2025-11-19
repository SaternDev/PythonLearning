# Durante la puesta en marcha de un servicio, el técnico debe asegurarse de que el archivo
# de configuración llamado “config.ini” existe en el directorio actual. Si el archivo no se
# encuentra o existe, pero no es un fichero, el script debe indicar que “falta el fichero”. Si
# existe, pero su tamaño es cero, debe avisar de que “el archivo está vacío”. Si existe y
# contiene información, debe confirmar que “el archivo es válido”.

from pathlib import Path

dirActual  = Path.cwd()
arhcivo = dirActual/'config.ini'

if Path.exists(arhcivo):
    if Path.is_file(arhcivo):
        if Path.stat(arhcivo).st_size == 0:
            print('El archivo está vacío')
        else:
            print('El archivo es válido')
    else:
        print('Falta el fichero')
else:
    print('El fichero no existe')