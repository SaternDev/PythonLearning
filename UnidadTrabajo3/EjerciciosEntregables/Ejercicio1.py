import sys
import shutil

#Pide (por argumento) un umbral de uso de disco en porcentaje (por ejemplo, 85). Obtén el uso de disco de la raíz y muestra:

if len(sys.argv) >= 2:
    humbral = int(sys.argv[1])
else:
    print('No se ha dado ningún número')

#Almacenar variables
total, usado, libre = shutil.disk_usage("/")

#Calcular el porcentaje
usoDiscPor = round((usado * 100) / total)

if (usoDiscPor < humbral):
    print('Alerta, estás usando más disco')
else:
    print('Ok')