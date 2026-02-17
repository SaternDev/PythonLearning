# Crea un fichero log.txt y añade (append) una línea con un mensaje y la hora actual.
# Ejecuta varias veces y comprueba que funciona correctamente.

from datetime import datetime

with open('log.txt', 'a') as f:
    f.write(f'La hora de ahora es: {datetime.now().time()} \n')