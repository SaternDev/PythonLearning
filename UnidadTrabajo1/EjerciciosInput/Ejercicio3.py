#La calculadora sencilla 
#Pide al usuario dos números. Muestra la suma, la resta, la multiplicación y la división.

numeroUno = float(input("Dime el primer número\n"))
numeroDos = float(input("Dime el segundo número\n"))
suma = numeroUno + numeroDos
resta = numeroUno - numeroDos
multiplicacion = numeroUno * numeroDos
division = numeroUno / numeroDos

print("La suma de los numeros es:", suma)
print("La resta de los numeros es:", resta)
print("La multiplicación de los numeros es:", multiplicacion)
print("La división de los numeros es:", division)