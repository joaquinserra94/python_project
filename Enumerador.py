#antes lo haciamos asi

lista = ['a','b','c']
indice = 0

for item in lista:
    print(indice,item)
    indice += 1

#con enumerador es mejor

lista = ['a','b','c']
for indice,item in enumerate(lista):
    print(indice,item)
    indice += 1

lista = ['a','b','c']
for item in enumerate(lista):
    print(item)
    indice += 1

lista = ['a','b','c']
for indice,item in enumerate(range(50,55)):
    print(indice,item)
    indice += 1

lista = ['a','b','c']
mis_tuples = list(enumerate(lista)) #asi creo una lista con tuplas dentro
print(mis_tuples)

lista = ['a','b','c']
mis_tuples = list(enumerate(lista))
print(mis_tuples[1][0])#si quiero acceder a algun elemento de mi tuple

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice, nombre in enumerate(lista_nombres):
    if nombre.startswith('M'):
        print(f"El nombre '{nombre}' comienza con M, su índice es: {indice}")

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice, nombre in enumerate(lista_nombres):
    if nombre.startswith('M'):
        print(indice)