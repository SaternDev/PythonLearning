# Pide el número de aulas (A) y el número de PCs por aula (P). Las carpetas esperadas en el sistema son (es decir, ya deben existir en el sistema, no las creamos):

# AULA-01/PC-01, AULA-01/PC-02, ..., AULA-0A/PC-0P
# Recorre la estructura de carpetas anterior y, para cada PC, si la carpeta existe, cuenta cuántos archivos .log hay dentro.

# Muestra para cada aula el total de .log encontrados y el total general al final.

# Librerías: from pathlib import Path

from pathlib import Path

countLog = 0
totalLog = 0

numAulas = int(input('Dime el número de aulas: '))
numPc = int(input('Dime el número de PCs por aula: '))
currentDir = Path.cwd()

for i in range(1, numAulas + 1):
    aulaDir = Path(str(currentDir) + '/' + "AULA-" + str(i).zfill(2))
    if aulaDir.is_dir():
        for b in range(1, numPc + 1):
            pcDir = Path(str(aulaDir) + '/' + "PC-" + str(b).zfill(2))
            if pcDir.is_dir():
                for c in pcDir.iterdir():
                    if str(c.name).endswith('.log'):
                        countLog += 1
                        totalLog += 1
                print(f'En PC-{str(b).zfill(2)} hay un total de {countLog} archivos ".log"')
                countLog = 0

print(f'El total de archivos ".log" es {totalLog}')
