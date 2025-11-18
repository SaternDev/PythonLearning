# Una persona se encuentra en el kilómetro 70 de una carretera, otra se encuentra en el km 150, los coches tienen sentido opuesto
#  y tienen la misma velocidad. Realizar un programa para determinar en qué kilómetro de esa carretera se encontrarán.

car1 = 70
car2= 150

while car1 != car2:
    car1 += 1
    car2 -= 1

print(f'Se encuentran en el kilometro {car1}km')