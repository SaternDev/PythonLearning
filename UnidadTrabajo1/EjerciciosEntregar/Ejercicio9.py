#Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuánto deberá pagar finalmente por su compra.

descuentoTotal = 0.15
precioCompra = float(input('Cuanto te has gastado en la compra?'))

totalConDescuento = precioCompra - (precioCompra * descuentoTotal)

print(f'El total con descuento es: {totalConDescuento}€')