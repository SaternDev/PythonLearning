#Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas,
#  el vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y 
# el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

sueldoBase = float(input('Cual es tu sueldo? '))
venta1 = float(input('Cuanto has ganado en tu primera venta? '))
venta2 = float(input('Cuanto has ganado en tu segunda venta? '))
venta3 = float(input('Cuanto has ganado en tu tercera venta? '))

comision = 0.10

totalRecibir = sueldoBase + (venta1 * comision + venta2 * comision + venta3 * comision )

print(f'El total que recibirá por las ventas este mes es: {totalRecibir}€')