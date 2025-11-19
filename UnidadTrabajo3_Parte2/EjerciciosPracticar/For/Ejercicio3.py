# Realizar un programa que pida números (se pedirá por teclado la cantidad de números a introducir).
#  El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.

numMayor = 0
numMenor = 0
NumIgual = 0

count = 0

numIntroduc = int(input('Dime la cantidad de números a introducir. \n'))

while True:
    if numIntroduc != 0:
        if count != numIntroduc:
            num = int(input('Dime un número: '))
            count += 1
            if num == 0:
                NumIgual += 1
            elif num < 0:
                numMenor += 1
            elif num > 0:
                numMayor += 1
        else:
            break
    else:
        print('Se ha introducido una cantidad de 0 números')
        break

if numIntroduc != 0:
    print(f'Numeros mayores a 0: {numMayor} \n Numeros menores a 0: {numMenor} \n Numeros iguales a 0: {NumIgual}')