# Hacer un programa que inicialice una lista de 10 números con valores aleatorios,
# y posteriormente ordene los elementos de menor a mayor en la misma lista utilizando una función concreta. 
# Deberá mostrarse la lista original y la ordenada.
import random


lista = []
lista.append(random.randint(0,1000))

while len(lista) != 10:
    lista.append(random.randint(0,1000))

lista.sort()
print(f'Los numeros ordenados es: {lista}')