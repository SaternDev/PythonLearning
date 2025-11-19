#Realizar un algoritmo que lea un número y que muestre su raíz cuadrada y su raíz cúbica. Utiliza potencias para ello.
#0.5, 0.25

num = float(input('Cual numero quieres usar?\n'))
raizCuadrada = num **  0.5
raizCubica = num ** 1/3
print(f'La raiz cuadrada de tu numero es {raizCuadrada} y la raiz cubica {raizCubica}')