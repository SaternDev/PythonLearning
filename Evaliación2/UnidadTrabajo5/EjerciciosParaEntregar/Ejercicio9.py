# Vas a simular la gestión de la variable de entorno PATH,
# que contiene varias rutas separadas por : (dos puntos).
# A partir de un string que representa un PATH, por ejemplo,
# "/usr/local/bin:/usr/bin:/bin" conviértelo en una lista,
# añade una nueva ruta al final (pídela por teclado), otra al inicio (pídela por teclado),
# y luego vuelve a unirlo en un solo string.
# Muestra cada una en una línea y luego muestra el resultado final.

from pathlib import Path
directorios = ['/usr/local/bin:/usr/bin:/bin']

primerRuta = input('Dime la ruta para el inicio: \n')
segundaRuta = input('Dime la ruta para el final: \n')

directorios.insert(0 ,primerRuta)
directorios.append(segundaRuta)

directorios = ':'.join(directorios)
directorios = directorios.split(':')

print(directorios)