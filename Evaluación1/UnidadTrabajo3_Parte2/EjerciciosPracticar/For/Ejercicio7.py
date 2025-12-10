# Escribe un programa que, dados dos números, uno real (base) y un entero positivo (exponente),
#  saque por pantalla el resultado de la potencia. No se puede utilizar el operador de potencia.
#  Para pedir el exponente, utiliza un bucle en el que obligues al usuario a introducir un número positivo.

num1 = int(input('Dime el numero de la base: '))
num2 = int(input('Dime el numero del exponente (Debe de ser en positivo): '))

while num2 < 0:
    num2 = int(input('No has puesto un numero positivo, dime de nuevo el exponente: '))
    expResult = num1 ** num2

print(f'El resultado de la potencia de {num1} elevado a {num2} es: {expResult}')