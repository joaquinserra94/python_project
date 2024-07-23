mi_tuple = 1,2,3,4 #podemos ponerlo con o sin parentesis
print(type(mi_tuple))

mi_tuple2 = (1,2,(10,20),3,4)
print(mi_tuple2[2])# tuple dentro de otro tuple

mi_tuple2 = list(mi_tuple2)
print(type(mi_tuple2))#hacemos casting y transformamos el tuple en lista

t = (1,2,3)
x,y,z = t
print(x,y,z)#aqui al tener la misma cantidad de variables que resultados se asigna una a cada una

g = (1,2,3,1)
print(len(g)) #cuenta el largo de la tupla
print(g.count(1)) #cuenta la cantidad de veces que aparece esta variable
print(g.index(2)) #te devuelve en que posicion esta