# Genera mediante un bucle 7 nombres de ficheros backup a partir de hoy en formato backup_AAAA_MM_DD.zip e imprímelos.

# Es decir, backup_2025_11_15.zip, backup_2025_11_16.zip, etc.

# Librerías: from datetime import datetime, timedelta

from datetime import datetime

fichero = ''
actualDate = datetime.now()
month = actualDate.month
day = actualDate.day

for _ in range(7):
    if day == 32:
        month += 1
        day = 1
    fichero = 'backup_' + str(actualDate.year) + '_' + str(month) + '_' + str(day) + '.zip'
    day += 1
    print(fichero)