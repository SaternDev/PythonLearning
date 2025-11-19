# Algoritmo que pida dos números e indique si el primero es mayor que el segundo o no.

num1 = float(input('Dime el primer número: '))
num2 = float(input('Dime el segundo número: '))

if num1 > num2:
    print(f'{num1} es mayor a {num2}')
else:
    print(f'{num1} es menor a {num2}')