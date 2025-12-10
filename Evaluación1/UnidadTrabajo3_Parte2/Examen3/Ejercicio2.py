# ================================================================
# PLANTILLA DE PLANIFICACIÓN DEL ALGORITMO (PSEUDOCÓDIGO)
# ================================================================

# ------------------------------------------------
# 1. COMPRENSIÓN DEL PROBLEMA
# ¿Qué me pide exactamente el enunciado?
# (Explica con tus palabras lo que el programa debe hacer.)
#
# Respuesta:
#

# ------------------------------------------------
# 2. DATOS DE ENTRADA
# ¿Qué información o valores necesita el programa?
# (Ejemplo: un número, una nota, un texto, etc.)
#
# Respuesta:
#

# ------------------------------------------------
# 3. DATOS DE SALIDA
# ¿Qué resultado debe mostrar el programa al usuario?
# (Ejemplo: “aprobado” o “suspenso”, “número par” o “impar”, etc.)
#
# Respuesta:
#

# ------------------------------------------------
# 4. CONDICIONES O DECISIONES
# ¿Qué comparaciones o decisiones tiene que tomar el programa?
# (Ejemplo: si la nota >= 5 entonces “Aprobado”, si no “Suspenso”.)
#
# Respuesta:
#

# ------------------------------------------------
# 5. ESTRUCTURA LÓGICA O PASOS DEL ALGORITMO (PSEUDOCÓDIGO)
# Escribe de forma breve los pasos que seguirá el programa.
# No uses sintaxis de Python, solo explica la lógica en orden.
#
# Ejemplo:
# Inicio
#   Leer ...
#   Si (condición) entonces
#       ...
#   Si no
#       ...
#   Mostrar resultado
# Fin
#
#

# ------------------------------------------------
# 6. COMPROBACIÓN MENTAL
# ¿Qué pasará si pruebo con un valor concreto?
# (Haz una prueba rápida mental o escrita.)
#
# Respuesta: si pruebo con 0 o un numero inferior debe de volver a pedir que introduzca de nuevo el número de archivos backup que quiero
#
# ================================================================
# A continuación escribe el código en Python debajo de esta línea:
# ================================================================



# Necesitamos un programa que cree una serie de carpetas de backup numeradas. Para 
# ello, pide un número N por teclado y crea las carpetas `backup_1` ... `backup_N` en 
# el directorio actual de trabajo. Si alguna ya existe, no pasa nada. Indica para cada 
# carpeta si la creas o si ya existía. Utiliza un bucle.

from pathlib import Path

numBackupFolder = int(input('Dime el número de carpetas de backup a crear: '))

currentDir = Path.cwd()

while numBackupFolder <= 0:
    print('Número de carpetas no aceptado, vuelve a introducirlo.')
    numBackupFolder = int(input('Dime el número de carpetas de backup a crear: '))

for i in range(1, numBackupFolder + 1):
    folderToCreate = Path(str(currentDir) + '/' + 'backup_' + str(i))
    if folderToCreate.is_dir():
        print(f'La carpeta {str(folderToCreate.name)} ya existe.')
    else:
        folderToCreate.mkdir()
        print(f'Se ha creado la carpeta: {str(folderToCreate.name)}.')