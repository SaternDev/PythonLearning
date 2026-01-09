# Crea un programa que pida un número de mes al usuario entre 1 y 12 (por ejemplo, el 4, que sería abril) 
# y diga cuántos días tiene (por ejemplo, 30) y el nombre del mes.
# Debes usar listas para guardar los días de los meses y los nombres.
# Para simplificarlo vamos a suponer que febrero tiene 28 días.
# Controla con un bucle while que el número de mes esté entre 1 y 12.

meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
diasMes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

numMes = int(input('Dime el número del mes: '))

while numMes < 1 or numMes > 12:
    print('Número de mes no adecuado.')
    numMes = int(input('Dime el número del mes: '))

print(f'El mes elegido es {meses[numMes - 1]} y tiene {diasMes[numMes - 1]} días')