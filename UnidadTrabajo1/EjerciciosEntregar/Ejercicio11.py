#Pide al usuario dos números y muestra la “distancia” entre ellos 
# (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).

primernumero = float(input('Cual es el primer número de distancia? '))
segundonumero = float(input('Cual es el segundo número de distancia? '))

diferenciaDistancia = abs(primernumero - segundonumero)
print(f'La distancia entre los números es: {diferenciaDistancia}')
