texto = "ABCDEFGHIJKLM"
fragmento = texto[2:5]
print(fragmento)

fragmento = texto[2:] #toma desde el numero 2 hasta el final
print(fragmento)

fragmento = texto[:5]#toma desde el comienzo hasta uno antes del quinto
print(fragmento)

fragmento = texto[2:10:2] #va tomando de a dos desde la posicion 2 hasta llegar al 10 sin incluirlo
print(fragmento)

fragmento = texto[::3] #toma todos de 3 en 3
print(fragmento)

fragmento = texto[::-1]
print(fragmento) #me devuelve la cadena al revés