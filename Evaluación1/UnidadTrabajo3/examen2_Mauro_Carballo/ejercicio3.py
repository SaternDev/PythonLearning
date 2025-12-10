# El responsable de copias de seguridad necesita saber si es un momento adecuado para
# hacer tareas de mantenimiento. El programa debe obtener la fecha y la hora actuales y
# decidir: si es fin de semana, mostrará que el sistema está en “ventana de
# mantenimiento”; si es un día laborable y antes de las 18 h, mostrará que el sistema está
# en “uso normal”; y si es más tarde, que el sistema entra en “modo nocturno”.

from datetime import datetime

print(f'La hora y fecha actual es: {datetime.now()}')

if datetime.now().weekday() >= 5:
    print('Ventana de mantenimiento')
elif datetime.now().weekday() < 5 and datetime.now().hour < 18:
    print('Sistema en uso normal')
else:
    print('El sistema está en modo nocturno')