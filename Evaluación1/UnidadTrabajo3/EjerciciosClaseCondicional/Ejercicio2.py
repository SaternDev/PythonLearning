# Algoritmo que pida un número y diga si es positivo, negativo o 0.

num = float(input('Dime tu numero: '))

if num == 0:
    print('Tu número es 0')
elif num > 0:
    print('Tu número es positivo')
elif num < 0:
    print('Tu número es negativo')