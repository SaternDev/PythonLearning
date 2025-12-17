from modulo_Mauro import *

print('PRUEBAS:')

#EJERCICIO 1
print('Función Mayores:')
n1 = 2
n2 = 3
n3 = -1
print(f'Pide dos números y indica el mayor (usamos {n1} y {n2})')

if mayores(n1,n2) == n1:
    print(f'{n1} es mayor a {n2}')
else:
    print(f'{n2} es mayor a {n1}')

print('es_par, manda true si es par, si nos manda false')
print(f'Usamos {n1}')

#EJERCICIO 3
if es_par(n1):
    print(f'{n1} es par')
else:
    print(f'{n1} es inpar')

#EJERCICIO 6
print('es_mayusculas, comprueba si la cadena dada es par o impar, devuelve true or false')
str1 = 'Prueba1'
str2 = 'PRUEBA2'

print(f'Probaremos con: {str1} y con {str2}')

if es_mayusculas(str1):
    print(f'{str1} está en mayusculas')
else:
    print(f'{str1} está en minusculas')

if es_mayusculas(str2):
    print(f'{str2} está en mayusculas')
else:
    print(f'{str2} está en minusculas')

#EJERCICIO 7
print(f'Función "potencia", requiere de dos parametros, la base y el exponente')

print(f'{n1} elevado a {n2} es: {potencia(n1,n2)}')

#EJERCICIO 9
print('Función "ordena_mayor_menor", reqyuere tres argumentos y los ordena de mayor a menor')

print(f'Usaremos: {n1}, {n2} y {n3}')
print(f'Ordenados: {ordena_mayor_menor(n1, n2, n3)}')

#EJERCICIO 10
print('Función "clasifica_circunferencias", indica si son: exteriores, tangentes exteriores, secantes, tangentes interiores, interiores o concéntricas. \n Requiere de 6 parametros: x1, y1, r1, x2, y2, r2')
x1 = 4
y1 = 6
r1 = 5

x2 = 7
y2 = 4
r2 = 8
print(f'x1 = {x1}, y1 = {y1}, r1 = {r1} y x2 = {x2}, y2 = {y2}, r2 = {r2}')

clasifica_circunferencias(x1,y1,r1,x2,y2,r2)

#EJERCICIO 11
print(f'FUnción "clasifica_triangulo". Clasifica el tipo de triangulo, necesita tres argumentos, devuelve el tipo de triangulo, usaremos {x1}, {x2} y {y2}')

clasifica_triangulo(x1,x2,y2)

#EJERCICIO 12
print('Función "es_bisiesto", hay que darle un solo argumento que será el año, devuelve true or false dependiendo de si es bisiesto o no')

anyo = 2024
anyo2 = 2026

print(f'Usaremos {anyo} y {anyo2}')

if es_bisiesto(anyo):
    print(f'El año {anyo} es bisiesto')
else:
    print(f'El año {anyo} no es bisiesto')

if es_bisiesto(anyo2):
    print(f'El año {anyo2} es bisiesto')
else:
    print(f'El año {anyo2} no es bisiesto')

#EJERCICIO 13
print(f'Función "es_fecha_correcta", devuelve true or false si la fecha existe o no, pide 3 argumentos, el día, mes y el año')

print('Día: 12, Mes: 7, Año: 2025')

if es_fecha_correcta(12,7,2025):
    print('La fecha es correcta')
else:
    print('La fecha es incorrecta')

#EJERCICIO 14
