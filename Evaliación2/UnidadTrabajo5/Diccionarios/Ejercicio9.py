# Escribe un programa que lea 5 frases introducidas por el usuario y almacene en un diccionario cuántas veces aparece cada palabra.
# Ignora mayúsculas/minúsculas.

palabrasFrase = []

palabrasCount = {

}

for _ in range(5):
    frase = input('Dime una frase: ')
    palabrasFrase = frase.split
    print(palabrasFrase)

    for i in range(0, len(palabrasFrase)):
        if palabrasFrase[i] in palabrasCount:
            palabrasCount[palabrasFrase[i]] = palabrasCount[palabrasFrase[i]] + 1
        else:
            palabrasCount[palabrasFrase[i]] = 0

    print(palabrasFrase)
print(palabrasCount)