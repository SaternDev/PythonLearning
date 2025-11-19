#Pista: find o index y [:]

#Dada una ruta como 'C:\\Users\\alumno\\Desktop\\proyecto', extrae: unidad 'C', usuario 'alumno' y carpeta 'Desktop' usando find/index y [:].
# Imprime cada uno de los valores.

route = 'C:\\Users\\alumno\\Desktop\\proyecto'
rest1 = route[route.find('\\') + 1:]
rest1 = rest1[rest1.find('\\') + 1:]
first_user = rest1[0:rest1.find('\\')]
carpet = rest1[rest1.find('\\') + 1:]
carpet = carpet[carpet.find('\\') + 1:]

print(f'Datos extraidos: Unidad: {route[0:1]}, Usuario: {first_user}, Carpeta: {carpet[:carpet.find('\\')]}')