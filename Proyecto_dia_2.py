nombre = input("Dime tu nombre: ")
ventas = float(input("venta del mes: "))
comision = round(ventas * 13 / 100, 2) #calculamos el 13% de comision
print(f"Ok {nombre} este mes vendiste: ${comision}")