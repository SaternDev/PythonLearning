# Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.

num1 = int(input('Dime el primer número'))
num2 = int(input('Dime el ultimo número'))

cont_numPar = 0

cont = num1

while cont < num2:
    if cont % 2 == 0:
        print('Es par')
        cont_numPar += 1
    cont += 1