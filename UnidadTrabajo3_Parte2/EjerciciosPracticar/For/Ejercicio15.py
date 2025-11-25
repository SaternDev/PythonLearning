# Una empresa les paga a sus empleados en base a las horas trabajadas durante la semana. 
# Realizar un programa para determinar el sueldo semanal de cada uno de los N trabajadores y, además,
#  calcular cuánto pagó la empresa por los N empleados en total.

# Pista: habrá que preguntar cuántos trabajadores tiene la empresa y cuánto es el sueldo por hora. Además, para cada trabajador,
#  tendrás que preguntar cuántas horas trabaja a la semana para calcular su sueldo.

numWorkers = int(input('Cuantos trabajadores hay en la empresa? \n'))
totalPayHour = round(float(input('Cuanto paga por hora la empresa? \n')), 2)

payHours = 0.

for i in (1, numWorkers + 1):
    WorkHours = round(float(input('Cuantas horas has trabajado? \n')), 1)
    payHours += WorkHours
    print(f'El trabajador {i} se le paga por la semana: {totalPayHour * WorkHours}')

print(f'La empresa tiene {numWorkers} trabajadores, la empresa tiene que pagar por todos ellos a la semana {payHours * totalPayHour}€')