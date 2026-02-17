# Crea (si no existe) un fichero admin_log.txt y añade una línea con fecha/hora (datetime) y un mensaje pedido por teclado.
#  No debe borrar el contenido anterior.

import os
from datetime import datetime

with open('admin_log.txt', 'a') as f:
    mensaje = input('Dime el mensaje: \n')
    f.write(f'{mensaje}: {datetime.now()}\n')