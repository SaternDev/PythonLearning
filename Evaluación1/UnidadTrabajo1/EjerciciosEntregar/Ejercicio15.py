#Dadas dos variables numéricas A y B, que el usuario debe teclear,
#  se pide realizar un algoritmo que intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables.

numA = int(input('Dime el primer número\n'))
numB = int(input('Dime el segundo número\n'))

aux = numA
numA = numB
numB = aux

print(f"Nuevo valor de A: {numA}")
print(f"Nuevo valor de B: {numB}")