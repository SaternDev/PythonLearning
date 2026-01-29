# Ejercicio 6: Usa shutil.disk_usage para mostrar en un diccionario el espacio total,
# usado y libre en GB (redondeando a un decimal) de tres rutas del sistema que pedirás por teclado.
# Muestra el contenido del diccionario recorriendo sus elementos.

import shutil
import os
from pathlib import Path

storage = {
    'total' : 0.,
    'usado' : 0.,
    'libre' : 0.
}

for _ in range(3):
    sistemDirect = input('Dime la ruta del sistema: \n')
    if Path(sistemDirect).is_dir():
        total, usado, libre = shutil.disk_usage(Path(sistemDirect))
        storage['total'] = round(total / (1024**3))
        storage['usado'] = round(usado / (1024**3))
        storage['libre'] = round(libre / (1024**3))

    for i in storage:
        print(f'El espacio {i} es: {storage[i]}GB')
