#Script que se elimina a si mismo

import sys
import os

archDocum = sys.argv[0]

agree = input('Se va a eliminar el script, estás seguro? (Si, No) \n')

if (agree == 'Si'):

    os.remove(archDocum)

print('Eliminando el Script')