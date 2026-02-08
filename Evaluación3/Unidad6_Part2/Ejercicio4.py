# Lee numeros.txt y calcula la suma de todos los números.

sum = 0

with open('numeros.txt' , 'r') as f:
    for i in f:
        i = int(i)
        sum += i
print(sum)