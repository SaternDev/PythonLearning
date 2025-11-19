# Crea un programa que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100 
# (utiliza la librería random).

# A continuación, va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido,
# además de los intentos que te quedan (tienes 10 intentos para acertarlo). El programa termina cuando se acierta el número
# (además te dice en cuantos intentos lo has acertado), si se llega al límite de intentos te muestra el número que había generado.

import random

numElegido = random.randrange(1,100)
numIntentos = 10

numAdivin = int(input('Dime un número: '))

while numAdivin != numElegido and numIntentos != 0:

    if numAdivin < numElegido:

        print('El número a adivinar es Mayor al número que has dicho')
        numIntentos -= 1
        print(f'Te quedan {numIntentos} intentos.')
        numAdivin = int(input('Dime otro número: '))

    elif numAdivin > numElegido:

        print('El número a adivinar es Menor al número que has dicho')
        numIntentos -= 1
        print(f'Te quedan {numIntentos} intentos.')
        numAdivin = int(input('Dime otro número: '))
    if numAdivin == numElegido:
        print(f'Has acertado, el número es {numAdivin}, lo has conseguido en {numIntentos} intentos.')
        break
else:
    print(f'Te has quedado sin intentos, el número elegido es: {numElegido}')