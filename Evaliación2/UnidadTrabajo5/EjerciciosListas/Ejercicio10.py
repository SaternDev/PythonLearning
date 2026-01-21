# Elabora un pequeño programa que gestionará una lista de la compra.
# El programa mostrará un menú con las opciones disponibles.
# Las opciones son las siguientes:

# Se trata de implementar cada una de las acciones.
# La opción 2 añade un solo elemento a la lista, por ejemplo, leche, mientras que la opción 5 es capaz de añadir
# varios elementos a la lista de una vez, escritos separados por coma, por ejemplo, cereales,jamón,agua
 

compra = []

#Mostrar menu 
print("\nGestión de Lista de la Compra") 
print("1. Mostrar la lista") 
print("2. Añadir elementos a la lista") 
print("3. Borrar elementos de la lista") 
print("4. Contar elementos de la lista") 
print("5. Añadir una lista de elementos a la ya existente") 
print("6. Borrar toda la lista") 
print("7. Salir")


while True:

    eleccion = int(input('Dime que opción quieres: '))
    
    if eleccion < 7 and eleccion > 0:
        if eleccion == 1:
            if len(compra) > 0:
                print(f'La lista de la compra es {', '.join(compra)}')
            else:
                print('La lista de la compra está vacia')
        elif eleccion == 2:
            productSel = input('Dime el producto que quieres: ')
            if productSel in compra:
                print('Ya existe el elemento')
            else:
                compra.append(productSel)
        elif eleccion == 3:
            print(f'Estos son los elementos añadidos a la lista: {compra}')
            elecDelet = input('Dime el elemento que quieres eliminar: ')
            if elecDelet in compra:
                print(f'Se ha eliminado {elecDelet}')
                compra.remove(elecDelet)
            else:
                print('El elemento no está en la lista')
        elif eleccion == 4:
            print(f'La cantidad de elementos en la lista es: {len(compra)}')
        elif eleccion == 5:
            segundaLista = []
            elemAñad = input('Dime los elementos que quieres añadir separados por comas: ')
            segundaLista = elemAñad.split(',')
            for i in segundaLista:
                if i in compra:
                    segundaLista.remove(i)
            if len(segundaLista) > 0:
                compra.extend(segundaLista)
        elif eleccion == 6:
            compra.clear
    else:
        if eleccion != 7:
            print('El numero no está en la lista')
            continue
        else:
            break