# Crea un fichero frases.txt y escribe 3 frases. Luego lee el fichero y muestra cada frase sin saltos de línea.

with open('frases.txt', 'r') as f:
    print(f.readlines())