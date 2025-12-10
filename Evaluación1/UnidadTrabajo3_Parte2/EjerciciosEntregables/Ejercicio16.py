# Pide una IP base tipo 192.168. (incluye el punto final).

# Pide el rango de subred (tercer octeto) inicio y fin, y el máximo host (último octeto).

# Para cada subred, muestra primero la gateway (x.x.<subred>.1) y luego los hosts del 2 al máximo,
# saltando los múltiplos de 5 (no asignables).

ipBase = input('Dime una IP de base tipo 192.168. (Incluye el punto final): ')
subredRange = int(input('Dime el rango de subred: '))
maxHostRange = int(input('Dime el rango máximo de host: '))

gateway = ipBase + str(subredRange) + '.' + '1'

if subredRange > 255 or subredRange < 0:
    print('Dirección de sub rango erronea')
    subredRange = int(input('Dime el rango de subred: '))

if maxHostRange < 1 or maxHostRange > 255:
    print('Máximo de rango host mal vuelve a escribirlo')
    maxHostRange = int(input('Dime el rango máximo de host: '))

print(f'La dirección de gateway es: {gateway}')

if maxHostRange > 1:
    for i in range(2, maxHostRange + 1):
        if i % 5 != 0:
            print(f'Dirección de subred: {ipBase}{subredRange}.{i}')
