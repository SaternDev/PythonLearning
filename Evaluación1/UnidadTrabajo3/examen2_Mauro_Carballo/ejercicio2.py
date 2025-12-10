# Un administrador quiere evaluar si el uso de espacio en disco de su unidad principal es
# aceptable o no. El programa debe analizar el porcentaje de espacio ocupado y mostrar
# un mensaje indicando si el estado es “OK”, “ADVERTENCIA” o “CRÍTICO”, según estos
# tres rangos: < 70 es “OK”, entre 70 y 89 mostrar “ADVERTENCIA” y si es 90 o más mostrar
# “CRÍTICO”.

#Espacio / total * 100

import shutil

total, used, free = shutil.disk_usage('/')

porcentajeUsado = round(used / total * 100)

if porcentajeUsado >= 90:
    print('Estado critico de uso de disco')
elif porcentajeUsado < 70:
    print('El estado del uso de disco es Ok')
else:
    print('El estado de uso del disco duro es Advertencia')