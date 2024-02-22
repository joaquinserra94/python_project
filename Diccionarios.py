diccionario = {'c1':'valor1','c2':'valor2'}
print(type(diccionario))
print(diccionario)

resultado = diccionario['c1']
print(resultado)

cliente = {'nombre':'Joaquin','apellido':'Serra','peso': 88 , 'talla': 1.86}
consulta = cliente['apellido']
print(consulta)

dic = {'c1':55, 'c2':[10,20,30],'c3':{'s1':100, 's2':200}}
print(dic['c2'])#aqui solo pido la definicion de la clave
print(dic['c2'][1])#aqui ya le pido que me busque dentro de la definicion y dentro de la lista que esta en la definicion

print(dic['c3'])
print(dic['c3']['s2'])

dic2 = {'c1':['a', 'b', 'c'],'c2':['d', 'e', 'f']}
print(dic2['c2'][1].upper())#imprimimos cambiando la letra a mayus

dic3 = {1:'a', 2:'b'}#para agregar un valor al diccionario
print(dic3)
dic3[3] = 'c'
print(dic3)
dic3[2] = 'B'
print(dic3) #para sobreescribir la clave

print(dic3.keys()) #para imprimir todas las claves
print(dic3.values()) #para imprimir todos los valores
print(dic3.items()) #nos devuelve todo los valores