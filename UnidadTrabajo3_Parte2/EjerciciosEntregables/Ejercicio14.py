# Pide el año (ej. 2025), el mes inicial y final (números del 1 al 12) y el número de días a crear por mes (ej. 5).
# Crea con pathlib la estructura de carpetas siguiente:

# backups/<AÑO>/<MM>/dia_<DD>

# Si una carpeta ya existe no pasa nada.
# Muestra por pantalla cada ruta creada.

# Ejemplo de ejecución: año=2025, mes_inicial=2, mes_final=4, num_días=3 generaría la siguiente estructura de carpetas:

# backups/2025/02/dia_01
# backups/2025/02/dia_02
# backups/2025/02/dia_03
# backups/2025/03/dia_01
# backups/2025/03/dia_02
# backups/2025/03/dia_03
# backups/2025/04/dia_01
# backups/2025/04/dia_02
# backups/2025/04/dia_03
# Librerías: from pathlib import Path

from pathlib import Path

year = input('Dime el año: ')
month = int(input('Dime el mes inicial del 1 al 12: '))
month2 = int(input('Dime el mes final del 1 al 12: '))
numDays = int(input('Dime el número de días: '))

actualDir = Path.cwd()
backupsDir = Path(str(actualDir) + '/' + 'backups')
yearDir = Path(str(actualDir) + '/' + str(year))

if month > month2:
    print('Has escrito un rango no adecuado para los meses, vuelve a indicarlos')
    month = int(input('Dime el mes inicial: '))
    month2 = int(input('Dime el mes final del 1 al 12: '))

if not backupsDir.is_dir():     
    Path.mkdir(Path('backups'))


for b in range(month, month2 + 1):

    monthDir = Path(str(yearDir) + '/' + str(b))

    if not yearDir.exists():
            Path.mkdir(Path('backups/' + str(year)))
    
    if not monthDir.exists():
        Path.mkdir(monthDir)

    for i in range(1, numDays + 1):
        dayDir = Path(str(monthDir) + '/' + 'dia_' + str(i))
        if not dayDir.exists():
            Path.mkdir(dayDir)