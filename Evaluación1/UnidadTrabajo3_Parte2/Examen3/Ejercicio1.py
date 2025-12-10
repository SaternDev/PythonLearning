# ================================================================
# PLANTILLA DE PLANIFICACIÓN DEL ALGORITMO (PSEUDOCÓDIGO)
# ================================================================

# ------------------------------------------------
# 1. COMPRENSIÓN DEL PROBLEMA
# ¿Qué me pide exactamente el enunciado?
# (Explica con tus palabras lo que el programa debe hacer.)
#
# Respuesta: Quiere comprobar cuales son los archivos que tienen cierta terminación y indicar cuantos tienen ciertas terminaciones u otras
#

# ------------------------------------------------
# 2. DATOS DE ENTRADA
# ¿Qué información o valores necesita el programa?
# (Ejemplo: un número, una nota, un texto, etc.)
#
# Respuesta: Una variable para cada tipo, una para las otras extensiones, una variable del directorio actual, otra con el nombre del archivo que se pide de backup
# y una más para la dirección del archivo al que comprobar si es un archivo
#

# ------------------------------------------------
# 3. DATOS DE SALIDA
# ¿Qué resultado debe mostrar el programa al usuario?
# (Ejemplo: “aprobado” o “suspenso”, “número par” o “impar”, etc.)
#
# Respuesta: Tiene que indicar el número de archivos que hay de cada tipo
#

# ------------------------------------------------
# 4. CONDICIONES O DECISIONES
# ¿Qué comparaciones o decisiones tiene que tomar el programa?
# (Ejemplo: si la nota >= 5 entonces “Aprobado”, si no “Suspenso”.)
#
# Respuesta: Primero el programa comprobará que el valor asignado no sea "FIN", seguido guardará en una variable el archivo,
#comprobará que el archivo exista; seguido de esto comprobará si es una de las diferentes terminologias.
#Condición de control de errores, va a comprobar si las variables de cada tipo de fichero no están a 0, dado que eso significaria dos cosas
#una, que no se ha introducido ningún archivo/no hay ningún archivo, o dos, que se ha introducido "FIN" en el comienzo del programa
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
# Respuesta: si pruebo con el archivo "prueba.zip" me indicará al final que hay 1 archivo terminado en ".zip"
#
# ================================================================
# A continuación escribe el código en Python debajo de esta línea:
# ================================================================


# Se necesita un programa que clasifique nombres de ficheros de backup por su extensión.
#  Para ello, realiza un programa que pida por teclado nombres de archivos de backup 
# hasta que el usuario introduzca la palabra FIN. 
# Cuenta cuántos terminan en `.zip` y cuántos terminan en `.tar.gz` o `.tgz`.
#  Cuenta también los archivos introducidos con cualquier otra extensión.  
# Al final, deberás imprimir cuántos archivos se han introducido de cada una de las tres categorías. 

# Nota: debes convertir los nombres de ficheros a objetos de tipo Path y comprobar
# previamente que existen y son ficheros para realizar el conteo.
from pathlib import Path


backupName = input('Dime un nombre de un archivo de backup, escribe "FIN" si queires detener el codigo: ')

currentDir = Path.cwd()

zipFile = 0
tarFile = 0
gzFile = 0
tgzFile = 0
otherExtension = 0

while backupName != 'FIN':

    for i in currentDir.iterdir():

        if str(i.name).startswith(backupName + '.'):
            backupFile = Path(str(currentDir) +  '/' + i.name)

            if backupFile.is_file():
                if str(backupFile.name).endswith('.zip'):
                    zipFile += 1
                elif str(backupFile.name).endswith('.tar'):
                    tarFile += 1
                elif str(backupFile.name).endswith('.gz'):
                    gzFile += 1
                elif str(backupFile.name).endswith('.tgz'):
                    tgzFile += 1
                else:
                    otherExtension += 1
    
    backupName = input('Dime un nombre de un archivo de backup, escribe "FIN" si queires detener el codigo: ')
else:
    
    if zipFile > 0 or tarFile > 0 or gzFile > 0 or tgzFile > 0 or otherExtension > 0:
        print(f'Hay una cantidad de archivos de backup que terminan por "zip" {zipFile}, por "tar" {tarFile}. por "gz" {gzFile} por "tgz" {tgzFile} y que terminen por otra extensión {otherExtension}')
    else:
        print('No se ha encontrado ningún archivo')