# El director de una escuela está organizando un viaje de estudios, 
# y requiere determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de viajes por el servicio.
#  La forma de cobrar es la siguiente: si son 100 alumnos o más, el costo por cada alumno es de 65 euros; de 50 a 99 alumnos,
#  el costo es de 70 euros, de 30 a 49, de 95 euros, y si son menos de 30, el costo de la renta del autobús es de 2850 euros,
#  sin importar el número de alumnos.
#  Realiza un programa que permita determinar el pago a la compañía de autobuses y lo que debe pagar cada alumno por el viaje.

cantAlummnos = int(input('Cual es la cantidad de alumnos: '))

if (cantAlummnos < 30):
    print(f'El  costo de la renta es: 2850 y cada alumno debe pagar {2850 / cantAlummnos}')
elif (cantAlummnos >= 100):
    print(f'El costo de bus es: {cantAlummnos * 65}€ y cada alumno debe pagar 65€')
elif (cantAlummnos <= 99 and cantAlummnos >= 50):
    print(f'El costo del bus es: {cantAlummnos * 70}€ y cada alumno debe pagar 70€')
elif (cantAlummnos <= 49 and cantAlummnos >= 30):
    print(f'El costo del bus es: {cantAlummnos * 95}€ y cada alumno debe pagar 95€')