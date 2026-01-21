# Escribe un programa que lea 5 frases introducidas por el usuario y almacene en un diccionario cuántas veces aparece cada palabra.
# Ignora mayúsculas/minúsculas.

palabrasFrase = []

palabrasCount = {

}

for _ in range(5):
    frase = input('Dime una frase: ')
    frase = frase.lower()
    palabrasFrase = frase.split()

    for i in palabrasFrase:
        if i in palabrasCount:
            palabrasCount[i] = palabrasCount[i] + 1
        else:
            palabrasCount[i] = 1

print(palabrasCount)