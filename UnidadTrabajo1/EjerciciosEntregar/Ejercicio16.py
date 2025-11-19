#Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d. 
# El que está detrás viaja a una velocidad mayor. 
# Se pide hacer un algoritmo para ingresar la distancia entre los dos vehículos (km) y sus respectivas velocidades (km/h) 
# y con esto determinar y mostrar en que tiempo (minutos) alcanzará el vehículo más rápido al otro.

velocidad1 = int(input('Cual es la velocidad en Km/h del primer vehiculo?\n'))
velocidad2 = int(input('Cual es la velocidad en Km/h del segundo vehiculo?\n'))
distancia = int(input('Cual es la distancai entre los vehiculos en Km? \n'))

tiempo_horas = (velocidad2 - velocidad1) / distancia

tiempo_minutos = tiempo_horas * 60

print(f"Lo alcanza en {tiempo_minutos:.f} minutos.")