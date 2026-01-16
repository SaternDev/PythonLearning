# Escribe un programa que cuente cuántas veces aparece cada letra en una palabra introducida por el usuario.
# Usa un diccionario para almacenar el resultado.
#  Ejemplo: en la palabra ‘amiga’ la ‘a’ aparece 2 veces, la ‘m’ 1 vez, la ‘i’ 1 vez y la ‘g’ 1 vez.

palabras = {

}

palabraSep = []

palabra = input('Dime una palabra: ')

palabraSep = list(palabra)
print(palabraSep)

for i in range(0, len(palabraSep)):
    if palabraSep[i] in palabras:
        palabras[palabraSep[i]] = palabras[palabraSep[i]] + 1
    else:
        palabras[palabraSep[i]] = 1

for j in palabras:
    print(f'La letra {j} se repite: {palabras[j]}')