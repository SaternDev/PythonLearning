with open('numeros.txt', 'r') as f:
    for i in f:
        i = int(i)
        if i % 2 == 0:
            print(i)