# Pistas: librería datetime

# Realiza un programa que averigue qué día de la semana es el día actual y muestre
# “Ventana de mantenimiento” si es sábado (día 5) o domingo (día 6). En caso contrario, muestra “Operación normal”.

# weekday()

from datetime import datetime

actualDay = datetime.today().weekday()

if actualDay == 5 or actualDay == 6:
    print('Ventana de mantenimiento')
else:
    print('Operación normal')