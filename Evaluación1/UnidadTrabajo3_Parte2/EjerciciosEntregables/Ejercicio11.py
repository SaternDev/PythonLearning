# Pide una IP base, por ejemplo ‘192.168.1.’ (debes incluir el punto final), y dos números: inicio y fin del último octeto.

# Muestra por pantalla las IPs con último octeto par entre ese rango (incluidos).

baseIP = input('Dime una IP de base: ')

starOctet = int(input('Dime el inicio del primer octeto: '))
endOctet = int(input('Dime el final del primer octeto: '))

for i in range(starOctet, endOctet + 1):
    if i % 2 == 0:
        print(f'La Ip es: {baseIP}{i}')