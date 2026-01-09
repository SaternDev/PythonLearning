# Realiza un programa que pida números enteros y los añada a una lista hasta que llegue a 10 elementos o
# se introduzca un número negativo. 
# A continuación, se debe imprimir la lista.

number = int(input('Dime el número que quieres que añada: '))

if number >= 0:
    lista = [number]

if lista is not None:
    while len(lista) != 10:
        number = int(input('Dime el número que quieres que añada: '))
        if number < 0:
            break

        lista.append(number)

if lista is not None:
    print(f'La lista es: {lista}')
else: 
    print('La lista está vacia')