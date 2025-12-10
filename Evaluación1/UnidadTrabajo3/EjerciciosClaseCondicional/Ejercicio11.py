# Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo.
#  El programa debe determinar qué tipo de triangulo es, teniendo en cuenta los siguiente:

# Si se cumple Pitágoras entonces es triángulo rectángulo
# Si sólo dos lados del triángulo son iguales entonces es isósceles.
# Si los 3 lados son iguales entonces es equilátero.
# Si no se cumple ninguna de las condiciones anteriores, es escaleno.

numA = int(input('Dime la primera dimensión del triangulo: '))
numB = int(input('Dime la segunda dimensión del triangulo: '))
numC = int(input('Dime la tercera dimensión del triangulo: '))

trianguloRec = bool(False)

#Formula Rectángulo
if((numA ** 2 == numB ** 2 + numC ** 2) or (numB ** 2  == numA ** 2 + numC ** 2) or (numC ** 2 == numA ** 2 + numB ** 2)):
    trianguloRec = True

#Decir cual triangulo es
if (trianguloRec):
    print('Es un triangulo rectangulo')

if(numA == numB == numC):
    print('Es un triangulo equilátero.')
elif(numA == numB or numA == numC or numB == numC):
    print('Es un triangulo Isósceles')
else:
    print('es un triangulo Escaleno')