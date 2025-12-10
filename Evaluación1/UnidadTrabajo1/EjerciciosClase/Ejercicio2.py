#Guarda el precio de una cena en una variable. Calcula el 10% de propina y múestralo.
precio_cena = 120.99
precio_propina = precio_cena * 0.10
total_pagar = precio_cena + precio_propina
print(precio_cena)
print("precio redondeado", str(round(precio_propina,0))+"€")
print("Precio total de la cena es:", str(round(total_pagar,2))+"€")