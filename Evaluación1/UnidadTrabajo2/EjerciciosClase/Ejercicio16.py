#Solicita al usuario que escriba una frase. Luego:

#1. Reemplaza todas las vocales (a, e, i, o, u) con asteriscos (*).

#2. Imprime la frase original y la frase modificada.

frase = str(input('Dime una frase: '))

fraseModificada = frase.replace('a','*')
fraseModificada = fraseModificada.replace('e', '*')
fraseModificada = fraseModificada.replace('i', '*')
fraseModificada = fraseModificada.replace('o', '*')
fraseModificada = fraseModificada.replace('u', '*')

print(f'Tu frase es: {frase}')
print(f'Tu frase modificada es: {fraseModificada}')