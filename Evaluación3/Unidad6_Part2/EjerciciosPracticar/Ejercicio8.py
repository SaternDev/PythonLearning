# Lee nombres.txt y muestra el nombre más largo.

nombreLargo = ''

with open('nombres.txt', 'r') as f:
    longitud = 0
    for i in f:
        if len(i) > longitud:
            longitud = len(i)
            nombreLargo = i
print(f'El nombre más largo es: {nombreLargo}')