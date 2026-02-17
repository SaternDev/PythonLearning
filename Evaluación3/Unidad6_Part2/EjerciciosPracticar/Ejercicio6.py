# Crea un fichero nombres.txt y guarda 5 nombres pedidos por teclado, uno por línea.

with open('nombres.txt', 'a') as f:
    for _ in range(5):
        nombre = input('Dime un nombres: ')
        f.write(nombre +'\n')