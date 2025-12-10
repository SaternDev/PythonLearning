# Ejercicio 4

# Programa que pida caracteres e imprima VOCAL si son vocales y NO VOCAL en caso contrario, el programa termina cuando 
# se introduce un espacio. Cuando pidas el carácter, asegúrate de que el usuario solo introduce un carácter (y no varios) con un bucle.

texto = str(input('Dime un caracter: '))

if len(texto) <= 1 and texto != " ":
    for _ in range(100000):
        if texto == '1' or texto == '2' or texto == '3' or texto == '4' or texto == '5' or texto == '6' or texto == '7' or texto == '8' or texto == '9' or texto == '0':
            print('No has escrito un caracter, vuelve a escribirlo.')
            texto = str(input('Dime un caracter: '))
            continue
        else:
            if texto == '':
                print('SE FINALIZA EL PROGRAMA')
                break
            elif texto == " ":
                print('SE FINALIZA EL PROGRAMA')
                break
            if len(texto)==1:
                if texto == 'a' or texto == 'e' or texto == 'i' or texto == 'o' or texto == 'u':
                    print('VOCAL')
                    texto = str(input('Dime otro caracter: '))
                else:
                    print('NO VOCAL')
                    texto = str(input('Dime un caracter: '))
                    continue
else:
    if len(texto) > 1:
        print('HAS ESCRITO MÁS DE UN CARACTER')
    elif texto == " ":
        print('NO HAS ESCRITO NINGÚN CARACTER')


# while len(texto) <= 1:
#     if texto == '1' or texto == '2' or texto == '3' or texto == '4' or texto == '5' or texto == '6' or texto == '7' or texto == '8' or texto == '9' or texto == '0':
#         print('No has escrito un caracter, vuelve a escribirlo.')
#         texto = str(input('Dime un caracter: '))
#         continue
#     else:
#         if texto == '':
#             print('SE FINALIZA EL PROGRAMA')
#             break
#         if len(texto)==1:
#             if texto == 'a' or texto == 'e' or texto == 'i' or texto == 'o' or texto == 'u':
#                 print('VOCAL')
#                 texto = str(input('Dime otro caracter: '))
#             else:
#                 print('NO VOCAL')
#                 texto = str(input('Dime un caracter: '))
#                 continue
# else:
#     if len(texto) > 1:
#         print('HAS ESCRITO MÁS DE UN CARACTER')
#     elif len(texto) < 1:
#         print('NO HAS ESCRITO NINGÚN CARACTER')
                