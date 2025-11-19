# Escribe un programa que pida el límite inferior y superior de un intervalo. Si el límite inferior es mayor que el superior 
# lo tiene que volver a pedir. A continuación, se van introduciendo números hasta que introduzcamos el 0.
#  Cuando termine el programa dará las siguientes informaciones:

# La suma de los números que están dentro del intervalo (intervalo abierto).
# Cuantos números están fuera del intervalo.
# Se informa si hemos introducido algún número igual a los límites del intervalo.

limInferior = int(input('Dime el limite inferior: '))
limSuperior = int(input('Dime el limite superior: '))

sumaNum = 0
numFuera = 0
numIgualLimit = 0

while limInferior < limSuperior:
    numIntroducido = int(input('Dime un número, para parar escribe 0: '))

    while numIntroducido != 0:
        if numIntroducido > limInferior and numIntroducido < limSuperior:
            sumaNum = sumaNum + numIntroducido
        elif numIntroducido == limInferior or numIntroducido == limSuperior:
            numIgualLimit += 1
        else:
            numFuera += 1
        numIntroducido = int(input('Dime otro número, para parar escribe 0: '))
    else:
        print(f'La suma de los numeros de dentro del intervalo es: {sumaNum}, los números fuera son {numFuera} y se ha introducido un numero igual a los limites {numIgualLimit} veces')
        break

        
else:

    print('El limite Inferior es superior al Limite Superior.')
    limInferior = int(input('Dime el limite inferior: '))
    limSuperior = int(input('Dime el limite superior: '))
    recountLimit = limInferior