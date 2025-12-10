# Pide por teclado un umbral de uso de disco (entre 0 y 100).

# Si no es válido, vuelve a pedirlo (máximo 3 intentos).

# A continuación, muestra el porcentaje real de uso de la raíz / y dí si supera o no el umbral.

# Librerías: import shutil
import shutil
from pathlib import Path

currentDirectory = Path.cwd()
totalDisc, usedDisc, freeDisc = shutil.disk_usage(currentDirectory)

print(totalDisc)
print(usedDisc)

usedDisc = int(usedDisc / totalDisc * 100)
print(usedDisc)

umbralUsage = int(input('Dime un umbral de uso de disco (entre 0 y 100):\n'))
tryes = 0


while umbralUsage < 0 or umbralUsage > 100 and tryes != 3:
    print('Me has dado un umbral erroneo')
    umbralUsage = int(input('Dime un umbral de uso de disco (entre 0 y 100):\n'))
    tryes += 1

print(f'El uso del disco es: {usedDisc}%')

if umbralUsage > usedDisc:
    print('El umbral es superior al uso del disco')
else:
    print('El umbral es inferior al uso del disco')