import random

lista_numeros = [0] * 10

for i in range(0, len(lista_numeros)):
    lista_numeros[i] = random.randint(1,10)

print(lista_numeros)