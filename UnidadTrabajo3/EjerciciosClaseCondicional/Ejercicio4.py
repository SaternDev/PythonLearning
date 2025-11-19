# Crea un programa que pida al usuario dos números y muestre su división si el segundo no es cero,
#  o un mensaje de aviso en caso contrario.

num1 = float(input('Dime el primer número: '))
num2 = float(input('Dime el segundo número: '))

if num2 != 0:
    print(f'La división entre los dos es: {num1/num2}')
elif num2 == 0:
    print('Tu segundo númro es 0, error.')