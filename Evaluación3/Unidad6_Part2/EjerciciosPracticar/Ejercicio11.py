# Lee palabras.txt y cuenta cuántas líneas tiene.

numLineas = 0

with open('palabras.txt', 'r') as f:
    for i in f:
        if i != '':
            numLineas += 1
print(f'El número de líneas es: {numLineas}')