# Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el exponente. Pueden ocurrir tres cosas:

# El exponente sea positivo, sólo tienes que imprimir la potencia.
# El exponente sea 0, el resultado es 1.
# El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.

numBase = int(input('Dime el número base: '))
numExp = int(input('Dime el número exponente: '))

if numExp > 0:
    print(f'Tu número da: {numBase**numExp}')
elif numExp == 0:
    print('Tu número da: 1')
elif numExp < 0:
    print(f'Tu número da: {(1/numBase) ** (numExp * -1)}')