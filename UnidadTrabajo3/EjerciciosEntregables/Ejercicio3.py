# Detecta e imprime el sistema operativo, la versión y el procesador del equipo en donde se ejecuta el script. A continuación,
#  muestra el gestor de paquetes recomendado según las siguientes indicaciones:

# Windows -> “winget”
# Linux -> “apt”
# macOS (Darwin) -> “brew”

# Para otros sistemas, muestra “gestor no definido”.

import platform

print(f'El sistema operativo es {platform.system()} versión {platform.release()}, el procesador del equipo es: {platform.processor()}')

if platform.system() == 'Windows':
    print('Utiliza el gestor de paquetes "winget"')
elif platform.system() == 'Linux':
    print('Utiliza el gestor de paquetes "apt"')
elif platform.system() == 'macOS':
    print('Utiliza el gestor de paquetes "brew"')
else:
    print('Gestor no definido')