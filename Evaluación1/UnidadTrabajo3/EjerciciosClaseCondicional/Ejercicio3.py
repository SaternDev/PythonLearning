#Escribe un programa que lea un número e indique si es par o impar.

num = float(input('Dime tu número: '))

if num % 2 == 0:
    print('Tu número es par')
elif num % 2 != 0:
    print('Tu número es impar')