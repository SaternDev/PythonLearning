# Dado un diccionario con productos y su precio, escribe un programa que calcule el precio total de una compra solicitando 
# al usuario qué productos desea y en qué cantidad mediante un bucle. El bucle terminará cuando el usuario introduzca la palabra ‘FIN’.
# Cuando el usuario escoja un producto, imprime el desglose del producto, la cantidad, el precio por unidad y precio total. 
# Al finalizar, imprime el total de la compra. Crea tú mismo el diccionario con al menos 4 pares producto-precio.

productos = {
    'manzana' : 10.,
    'pollo' : 16.20,
    'patatas' : 7.50,
    'aceite' : 10.
}

totalCompra = 0.
productSelect = ''

while True:

    if productSelect != '':  
        if productSelect == 'FIN':
                break

    productSelect = input('Dime el producto que deseas (Escribe FIN para terminar la compra): ')

    if productSelect == 'FIN':
                break

    while productSelect not in productos:
        print('El producto elegido no existe')
        productSelect = input('Dime el producto que deseas (Escribe FIN para terminar la compra): ')

    cantidadProduct = int(input(f'Dime cuantos quieres de {productSelect}: '))
    if cantidadProduct != 0:
         
        for _ in range(cantidadProduct):
            totalCompra += productos[productSelect]

print(f'El total de tu compra es: {totalCompra}€')