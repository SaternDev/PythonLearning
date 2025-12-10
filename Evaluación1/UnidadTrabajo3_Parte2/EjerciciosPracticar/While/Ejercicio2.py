# Programa que pida números hasta que se introduzca un cero. Debe imprimir la suma y la media de todos los números introducidos.

suma = 0
contNum = 0

#Pido al usuario el primer número
num = int(input('Dame un número, si quieres termianr el programa escribe "0"\n'))

#Hago un bucle que se reproduce mientras no hayamos introducido 0
while num != 0:
    #Reescribimos variable para realizar la suma de cada num dado
    suma = suma + num
    #Vamos añadiendo la cuenta de los números
    contNum += 1
    num = int(input('Dame un número, si quieres termianr el programa escribe "0"\n'))

#Este if lo tenemos para asegurarnos que no pete si es que escriben 0 al principio del programa
if num == 0:
    print('No se ejecuta el programa dado que se ha escrito 0 al principio.')
    print(f'La suma de los numeros es: {suma}, y la media de todos los numeros es: {suma/contNum}')
    