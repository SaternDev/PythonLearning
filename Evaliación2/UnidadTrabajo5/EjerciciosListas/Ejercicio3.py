# Realiza un programa que lea por teclado las 5 notas obtenidas por un alumno.
# Debes controlar que las notas estén comprendidas entre 0 y 10 y pueden contener decimales.
# A continuación, debe mostrar todas las notas indicando su orden, es decir, “Nota 1: 5.5, Nota 2: 6, …”,
# debe mostrar también la nota media, la nota más alta que ha sacado y la menor.

list_notas = [0] * 5

for i in range(0,5):
    nota = int(input('Dime la nota: '))
    while nota < 0 or nota > 10:
        nota = int(input('La nota no es válida, dime una válida: '))
    list_notas[i] = nota

for i in range(0, len(list_notas)):
    print(f'Nota {i}: {list_notas[i]}')