# Queremos guardar los nombres y las edades de los alumnos de un curso.
# Para ello utilizarás dos listas, una para nombres y otra para edades.
# Realiza un programa que introduzca el nombre y la edad de cada alumno.
# El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (*)
# Al finalizar se mostrará los siguientes datos:

# Todos los alumnos mayores de edad (su nombre y edad).
# Los alumnos mayores, es decir, los que tienen más edad (su nombre y edad).

nombres = []
edades = []

while True:
    name = input('Dime el primer nombre: ')

    if name == '*':
        break

    nombres.append(name)
    age = int(input('Dime la edad de ese alumno: '))
    edades.append(age)

for i in range(0, len(edades)):
    if edades[i] >= 18:
        print(f'{nombres[i]} tiene {edades[i]}')