# Crea un programa que pida un número y calcule su factorial 
# (El factorial de un número es el producto de todos los enteros entre 1 y el propio número y se representa por el número seguido 
# de un signo de exclamación. Por ejemplo 5! = 1x2x3x4x5=120).

num = int(input('Dime tu número.\n'))
numMod = num
i = 1

if num !=0:

    for _ in range(1, num):
        numMod = numMod * i
        i += 1
    print(f'El factorial de {num}! = {numMod}')
else:
    print('El número es 0')