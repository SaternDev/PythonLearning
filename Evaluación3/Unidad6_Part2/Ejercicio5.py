# Simula una configuración en service.conf guardando en el fichero líneas clave=valor.
# Por ejemplo: port=8080, mode=prod, user=admin. Léelo y crea un diccionario.
# Luego pregunta una clave por teclado y muestra su valor o un mensaje si no existe.

diccionario = {

}

with open('service.conf', 'r') as f:
    for linea in f:
        clave, valor = linea.strip().split('=')
        diccionario[clave] = valor

selected = input('Dime la clave que quieres buscar: ')

if selected in diccionario:
    print(f'El valor de la clave {selected} es: {diccionario[selected]}')
else:
    print('No existe la clave')