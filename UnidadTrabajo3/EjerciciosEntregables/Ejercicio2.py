# Pistas: librería datetime

# Vamos a organizar los backups según la hora. Obtén la hora actual y muestra:

# “Backup de mañana” si hora < 12
# “Backup de tarde” si 12 <= hora < 20
# “Backup nocturno” si hora >= 20

from datetime import datetime

horaActual = datetime.now().hour

if horaActual < 12:
    print('Backup de mañana')
elif 12 <= horaActual < 20:
    'Backup de tarde'
elif horaActual >= 20:
    'Backup nocturno'