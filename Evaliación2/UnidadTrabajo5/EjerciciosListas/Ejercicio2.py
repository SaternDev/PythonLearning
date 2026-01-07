#Crea una lista de 5 elementos donde cada elemento sea una cadena que se pide por el teclado. 
# Copia los elementos de la lista en otra lista, pero en orden inverso, y muestra los elementos invertidos por la pantalla.

test_list = [''] * 5
lista_dos = []

for i in range(0, len(test_list)):
    test_list[i] = input(f'Dime que elemento quieres para el elemento {i}: ')

print(test_list)

lista_dos = test_list[::-1]

print(lista_dos)