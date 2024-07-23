mi_lista = ["a", "b", "c"]
print(type(mi_lista))
print(len(mi_lista))
resultado = mi_lista [0]
print(resultado)
mi_lista2 = ["d", "e", "f"]

mi_lista3 = mi_lista + mi_lista2

mi_lista3[0] = 'alfa' #a diferencia de los strings, aqui podemos cambiar los elementos de la lista
mi_lista3.append('g') #para agregar un elemento a la lista
print(mi_lista3)
mi_lista3.pop() #si lo dejamos bacio, nos elimina el ultimo elemento
print(mi_lista3)
eliminado = mi_lista3.pop(0) #borramos el elemento "cero" de la lista y si lo establecemos en una variable, nos lo guarda para mas adelante
print(mi_lista3)
print(eliminado, "es tu palabra eliminada y guardada en la variable")

lista = ["g","o","b","m","c"]
lista.sort()#esto lo ordena, en este caso: alfabeticamente
print(lista)
lista.reverse()#lo ordena porque esta el sort anteriormente pero en este caso, lo da vuelta
print(lista)


