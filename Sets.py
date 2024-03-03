mi_set = set([1,2,3,4,5]) #podemos declarar el set entre parentesis con la palabra set
print(type(mi_set))
print(mi_set)

otro_set = {1,2,3} #o tambien, podemos declarar un set solo entre llaves
print(type(otro_set))
print(otro_set)

mi_set2 = set([1,2,3,4,5,2,2,2,2,2]) #no admite elementos repetidos, simplemente los borra
print(type(mi_set2))
print(mi_set2)

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2) #unimos dos sets con .union
print(s3)

q1 = {1,2,3}
q1.add(4) #agregamos un elemento con .add
print(q1)

q2 = {1,2,3}
q2.remove(3) #quitamos un elemento con remove
print(q2)

q3 = {1,2,3}
q3.pop() #elimina un elemenro aleatorio, si lo guardamos en una variable podria usarse como sorteo
print(q3)