#Pide al usuario dos pares de números x1, y1 y x2, y2, que representen dos puntos en el plano. Calcula y muestra la distancia entre ellos.

x1 = float(input('Dime el primer numero del primer par de números '))
y1 = float(input('Dime el segundo numero del primer par de números '))
x2 = float(input('Dime el primer numero del segundo par de números '))
y2 = float(input('Dime el segundo numero del segundo par de números '))

distancia = (((x2 - x1)**2 + (y2 - y1)**2))**0.5

print(f'Distancia: {distancia:.2f}')