# Pistas: sys.argv

# Dado un hostname (que se pide como argumento), muestra:

# “VÁLIDO” si empieza por “PC-“ y su longitud es al menos 7
# “NO VÁLIDO” en caso contrario

import sys

if len(sys.argv) >= 2:
    hostname = sys.argv[1]
    hostname = str(hostname)
    if hostname.startswith('PC-') and len(hostname) >= 7:
        print('Hostname VÁLIDO')
    else:
        print('Hostname no valido')
else:
    print('No se ha dado ningún argumento')