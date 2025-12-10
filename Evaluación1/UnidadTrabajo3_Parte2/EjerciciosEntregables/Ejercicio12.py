# Pide una contraseña repetidamente hasta que cumpla los siguientes criterios:

# Tiene al menos 6 caracteres
# Contiene al menos un dígito

# Usa un bucle whilepara repetir la contraseña y un for para comprobar si algún carácter es dígito.

contraseña = input('Dime una contraseña: ')

if contraseña.isnumeric():
    print('Lo es')

while True:
    if len(contraseña) > 6 and '1' in contraseña or '2' in contraseña or '3' in contraseña or '4' in contraseña or '5' in contraseña or '6' in contraseña or '7' in contraseña or '8' in contraseña or '9' in contraseña or '0' in contraseña:
        print('Es correcta')
        break
    else:
        contraseña = input('La contraseña es incorrecta, dime otra contraseña que cumpla los requisitos: ')