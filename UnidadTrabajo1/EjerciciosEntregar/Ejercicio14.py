#Dado un número entero de dos cifras, 
# diseñe un algoritmo que permita obtener el número invertido utilizando operaciones aritméticas.
#  Ejemplo, si se introduce 23 que muestre 32

num = int(input('Dime el numero de dos decimales\n'))

operacionPrimNum = num // 10
operacionSegNum = num % 10
operacionFinal = operacionSegNum * 10 + operacionPrimNum

print(f'Tu número invertido es: {operacionFinal}')