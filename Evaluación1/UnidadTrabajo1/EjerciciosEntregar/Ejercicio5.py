#Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. Recordar que la fórmula para la conversión es:
#
# C = (F-32)*5/9

gradosFahrenheit = float(input('Cuantos Cº Fahrenheit tengo que convertir a Grados Celsius?\n'))

conversionCelcius = (gradosFahrenheit - 32) * 5/9
print(gradosFahrenheit, 'en grados celsius es:', conversionCelcius)