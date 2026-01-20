#  Dado un texto introducido por teclado, muestra cuántas veces aparece cada vocal usando un diccionario.
#  Usa una sola pasada sobre el texto.

vocales = {
    'a' : 0,
    'e' : 0,
    'i' : 0,
    'o' : 0,
    'u' : 0
}

texto = input('Dime un texto: ')
texto = texto.lower()

for i in texto:
    if i in vocales:
        vocales[i] += 1

print(f'EL numero de veces por vocal es: {vocales}')