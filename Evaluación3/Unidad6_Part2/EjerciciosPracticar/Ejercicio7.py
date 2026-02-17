# Lee nombres.txt y muestra cuántos nombres hay.

count = 0

with open('nombres.txt', 'r') as f:
    for i in f:
        if i != '':
            count += 1

print(f'La cantidad de nombres es: {count}')