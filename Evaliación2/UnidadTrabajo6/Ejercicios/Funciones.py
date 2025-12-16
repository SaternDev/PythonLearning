
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
def calcula_ganancias_uva(precio_kilo, kilos, tipo, tamanyo):
    precio_inicial = precio_kilo
    kilos = int(input("Introduce cuántos kilos has vendido: "))
    tipo = input("Introduce el tipo de la UVA (A/B): ").upper()

    #if tipo not in ["A", "B"]:
    if tipo != "A" and tipo != "B":
        print("Tipo incorrecto")
    else:
        tamanyo

        #if tamanyo not in ["1", "2"]:
        if tamanyo != "1" and tamanyo != "2":
            print("Tamaño incorrecto")
        else:
            if tipo == "A":
                if tamanyo == "1":
                    precio_inicial += 20
                else:  # Tamaño "2"
                    precio_inicial += 30
            elif tipo == "B":
                if tamanyo == "1":
                    precio_inicial -= 30
                else:  # Tamaño "2"
                    precio_inicial -= 50

            precio_final = precio_inicial * kilos

            print(f"La ganancia es {precio_final / 100:.2f} euros.")

#Ejercicio 15
def costes_viaje(n):
    cantAlummnos = n

    if (cantAlummnos < 30):
        print(f'El  costo de la renta es: 2850 y cada alumno debe pagar {2850 / cantAlummnos}')
    elif (cantAlummnos >= 100):
        print(f'El costo de bus es: {cantAlummnos * 65}€ y cada alumno debe pagar 65€')
    elif (cantAlummnos <= 99 and cantAlummnos >= 50):
        print(f'El costo del bus es: {cantAlummnos * 70}€ y cada alumno debe pagar 70€')
    elif (cantAlummnos <= 49 and cantAlummnos >= 30):
        print(f'El costo del bus es: {cantAlummnos * 95}€ y cada alumno debe pagar 95€')

#Ejercicio 16
def coste_llamada(tiempo, es_domingo, turno):

    coste = 0.0 #tipo float

    if tiempo <= 5:
        coste = tiempo * 100
    elif tiempo <= 8: #minuto 6, 7 y 8 a 80 céntimos
        coste = (tiempo - 5) * 80 + 500
    elif tiempo <= 10: #minuto 9 y 10 a 70 céntimos
        coste = (tiempo - 8) * 70 + 240 + 500
    else: #minutos 11 y sucesivos a 50 
        coste = (tiempo - 10) * 50 + 140 + 240 + 500

    if es_domingo == "S":
        coste += coste * 0.03  # 3% adicional
    else:
        if turno == "M":
            coste += coste * 0.15  # 15% adicional
        elif turno == "T":
            coste += coste * 0.10  # 10% adicional

    print(f"El coste de la llamada es: {coste / 100:.2f} euros.")

#Ejercicio 16
def dia_escrito(n):
    dia = n

    if dia == 1:
        print("Lunes")
    elif dia == 2:
        print("Martes")
    elif dia == 3:
        print("Miércoles")
    elif dia == 4:
        print("Jueves")
    elif dia == 5:
        print("Viernes")
    elif dia == 6:
        print("Sábado")
    elif dia == 7:
        print("Domingo")
    else:
        print("Día incorrecto")

#Ejercicio 19
def num_dias_mes(mes):
    #if mes in [1, 3, 5, 7, 8, 10, 12]:
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        print("31 días")
    elif mes == 2:
        print("28 o 29 días")
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    #elif mes in [4, 6, 9, 11]:
        print("30 días")
    else:
        print("Mes incorrecto")

#Ejercicio 20
def calcula_coste_transporte(peso, zona):
    if peso > 0 and peso <= 5000:
        print("1.- América del Norte")
        print("2.- América Central")
        print("3.- América del Sur")
        print("4.- Europa")
        print("5.- Asia")
        
        zona = int(input("¿A qué zona se reparte (1-5)?: "))
        
        if zona == 1:
            print(f"Coste: {peso * 24 / 100:.2f} euros.")
        elif zona == 2:
            print(f"Coste: {peso * 20 / 100:.2f} euros.")
        elif zona == 3:
            print(f"Coste: {peso * 21 / 100:.2f} euros.")
        elif zona == 4:
            print(f"Coste: {peso * 10 / 100:.2f} euros.")
        elif zona == 5:
            print(f"Coste: {peso * 18 / 100:.2f} euros.")
        else:
            print("Zona incorrecta.")
    else:
        print("Peso incorrecto (no podemos transportar paquetes de más de 5Kg).")