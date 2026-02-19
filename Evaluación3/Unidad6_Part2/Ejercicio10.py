# Programa que recibe por sys.argv el nombre de un fichero de texto.
# Debe imprimir el número de líneas, palabras y caracteres del fichero (si no existe, mostrar un error amigable).

from pathlib import Path
import sys

caracteres = 0
frase = ''
palabras = 0

fichero = sys.argv[1]

print(fichero)

if Path(fichero).is_file():
    with open(fichero, 'r') as f:
        
        for line_n, line in enumerate(f, start=1):
            for i in line:
                caracteres += 1
                
    with open(fichero, 'r') as f:

        for j in f.readlines():
            frase = frase + ' ' + j.strip()

        for character in frase:
            if character == ' ':
                palabras += 1
        
        print(f'El número de líneas es {line_n}, tiene {palabras} palabras, cotiene {caracteres} caracteres.')
else:
    print('ERROR: El fichero no existe')