# Realiza un programa que muestre la tabla de multiplicar de los números 1,2,3,4 y 5. Utiliza un bucle anidado.

multTable = 1

for n in range(1, 6):
    for i in range(1,11):
        print(f'{n} * {i} = {n * i}')
        i += 1
        if i == 11:
            i = 1
    n += 1