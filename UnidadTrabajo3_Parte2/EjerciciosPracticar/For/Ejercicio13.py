#Una empresa quiere tener el registro de las horas que trabaja diariamente un empleado durante la semana (seis días)
#  para determinar el total de éstas, así como el sueldo que recibirá por las horas trabajadas. 
# Por tanto, deberás pedir por teclado cuantas horas ha trabajado cada día, así como a cuánto cobra la hora. El precio por hora es único.

hourWork = 0
totalHourWork = 0
hourPay = 0
totalHourPay = 0

for _ in range(6):
    hourWork = round(float(input('Cuantas horas has trabajado? \n')),1)
    totalHourWork += hourWork
    hourPay = round(float(input('A cuanto has conbrado las horas? \n')), 2)
    totalHourPay += hourPay

print(f'Ha hecho: {totalHourWork}h totales en la semana y ha cobrado: {totalHourPay}€')