#Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde. 
#Por ejemplo: 1000 minutos son 16 horas y 40 minutos.

minutosPedidos = int(input('Cuantos minutos quieres convertir?'))
horas = minutosPedidos // 60
calculoMin = (minutosPedidos % 60)
calculoHorasiMinutos = round(horas) 

print('La cantidad de horas', horas, 'Cantidad de minutos', calculoMin)