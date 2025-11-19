#Realizar un programa que muestre la tabla de multiplicar de un número introducido por teclado.

numMulti = int(input('Dime el número del cual quieras su tabla de multiplicar: '))

contador = 0

while contador != 11:
    resMulti = numMulti * contador
    print(f'{numMulti} * {contador} = {resMulti}')
    contador += 1