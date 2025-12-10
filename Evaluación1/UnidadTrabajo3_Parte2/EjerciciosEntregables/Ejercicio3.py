# Pide mediante un bucle while hostnames al usuario hasta que escriba FIN.

# Cuenta cuántos has introducido y muestra el total al final.

# No uses listas; solo un contador y cadenas.

hostname = input('Dime un hostname, si quieres que termine el programa pon "FIN": ')
count = 0

while hostname != 'FIN':
    hostname = input('Dime un hostname, si quieres que termine el programa pon "FIN": ')
    count += 1

print(f'La cantidad de hostnames es: {count}')