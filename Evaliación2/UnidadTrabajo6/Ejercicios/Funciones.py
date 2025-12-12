
#Ejercicio1
def mayores(n1,n2):
    if n1 > n2:
        return n1
    else:
        return n2
    
#Ejercicio3
def es_par(n):
    if n % 2 == 0:
        return True
    else:
        return False

#Ejercicio6
def es_mayusculas(cad):
    if str(cad).isupper():
        return True
    else:
        return False

#Ejercicio7
def potencia(base, exp):
    return base ** exp

#Ejercicio9
def ordena_mayor_menor(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        if n2 >= n3:
            return n1, n2, n3
        else:
            return n1, n3, n2
    elif n2 >= n1 and n2 >= n3:
        if n1 >= n3:
            return n2, n1, n3
        else:
            return n2, n3, n1
    else:
        if n1 >= n2:
            return n3, n1, n2
        else:
            return n3, n2, n1

#Ejercicio10
def clasifica_circunferencias(x1, y1, r1, x2, y2, r2):
    import math
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    if distancia > (r1 + r2):
        print("Circunferencias exteriores")
    elif distancia == (r1 + r2):
        print("Circunferencias tangentes exteriores")
    elif distancia < (r1 + r2) and distancia > abs(r1 - r2):
        print("Circunferencias secantes")
    elif distancia == abs(r1 - r2):
        print("Circunferencias tangentes interiores")
    elif distancia > 0 and distancia < abs(r1 - r2):
        print("Circunferencias interiores")
    elif distancia == 0:
        print("Circunferencias concéntricas")

#Ejercicio11
def clasifica_triangulo(a,b,c):
    if (a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (c**2 + a**2 == b**2):
        print("Triángulo Rectángulo")

    if a == b == c:
        print("Triángulo Equilátero")

    elif (a == b) or (b == c) or (c == a):
        print("Triángulo Isósceles")

    else:
        print("Triángulo Escaleno")

#Ejercicio12
def es_bisiesto(anyo):
    if (anyo % 4 == 0 and anyo % 100 != 0 or anyo % 400 == 0):
        return True
    else:
        return False

#Ejercicio13
def es_fecha_correcta(dia, mes, anyo):

    #if mes in [1, 3, 5, 7, 8, 10, 12]:
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        dias_del_mes = 31
    #elif mes in [4, 6, 9, 11]:
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        dias_del_mes = 30
    elif mes == 2:
        #  bisiesto
        if (anyo % 4 == 0 and not (anyo % 100 == 0)) or (anyo % 400 == 0):
            dias_del_mes = 29
        else:
            dias_del_mes = 28
    else:
        return False

    if dia < 1 or dia > dias_del_mes:
        return False
    else:
        return True
    
#Ejercicio14
