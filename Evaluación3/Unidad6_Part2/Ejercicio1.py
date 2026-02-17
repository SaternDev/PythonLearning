# Genera un informe system_report.txt con la fecha/hora actual, 
# el sistema operativo detectado (platform) y el número de CPUs (os.cpu_count()).

import os
import platform
from datetime import datetime

with open('system_report.txt', 'a') as f:
    f.write(f'La fecha y hora es: {datetime.now()}\n')
    f.write(f'El sistema operativo es: {platform.system()}\n')
    f.write(f'El numero de CPUs es {os.cpu_count()}')