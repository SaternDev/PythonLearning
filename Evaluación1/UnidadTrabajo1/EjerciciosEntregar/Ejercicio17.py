#Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos.
#  El tiempo de viaje hasta llegar a otra ciudad B es de T segundos.
#  Escribir un algoritmo que determine la hora de llegada a la ciudad B.

tiempoHorasIda =  int(input("Hora de salida (HH): "))
tiempoMinutpsIda =  int(input("Hora de salida (MM): "))
tiempoSegundosIda =  int(input("Hora de salida (HH): "))

segviaje = int(input("Tiempo que has tardado en segundos: "))

segundosIniciales = tiempoHorasIda * 3600 + tiempoMinutpsIda * 60 + tiempoSegundosIda

segundosFinales = segundosIniciales + segviaje

