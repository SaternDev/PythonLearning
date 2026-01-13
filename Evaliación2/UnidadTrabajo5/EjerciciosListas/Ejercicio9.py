# Queremos guardar la temperatura mínima y máxima de los 7 días de la semana pasada en dos listas.
# Para ello pide las temperaturas por teclado. Realiza un programa que dé la siguiente información:

# Calcule la temperatura media de cada día.

# Calcule los días con menos temperatura.

# Lea una temperatura por teclado y se muestre los días cuya temperatura máxima coincide con ella.
# Si no existe ningún día se mostrará un mensaje informativo.

# Nota: Como implementación básica, nos podemos referir a los días por su número 
# (por ejemplo, el día 1 el lunes, el 2 es martes, etc). Si queréis mejorar el programa,
# nos referiremos por su nombre (lunes, martes, etc.)

diasSem = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']

tempMin = []
tempMax = []
tempMed = []

for _ in range(0,7):
    temp1 = int(input('Dime la temperatura máxima del día: '))
    tempMax.append(temp1)

    temp2 = int(input('Dime la temperatura minima del día: '))
    tempMin.append(temp2)

    tempMed.append((temp1 + temp2)/2)

for j in range(0,7):
    print(f'La temperatura media de {diasSem[j]} es {tempMed[j]}')

tempSearch = int(input('Dime una temperatura máxima que revise si coincide: '))

for i in range(0,7):
    if tempMax[i] == tempSearch:
        print(f'Tu temperatura máxima coincide con el {diasSem[i]}')

tempMasBaja = min(tempMin)

for i in range(0,7):
    print('Los días con menos temperatura son:')
    if tempMin[i] == tempMasBaja:
        print(diasSem[i])

print(tempMin)
print(tempMax)
print(tempMed)