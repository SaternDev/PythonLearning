# Ejercicio 1: Muestra información del sistema operativo (sistema, versión, nodo y procesador) y almacena los datos en un diccionario.
# Crea una lista con los valores y muéstralos ordenados alfabéticamente.

import platform

systemInfo = {

}

listaInfo = []

systemInfo["System"] = platform.system()
systemInfo["Version"] = platform.release()
systemInfo["Processor"] = platform.processor()

for i in systemInfo:
    listaInfo.append(systemInfo[i])

listaInfo.sort()

print(listaInfo)