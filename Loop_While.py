monedas = 5
while monedas > 0:
    print(f'tengo {monedas} monedas')
    monedas = monedas - 1
    #monedas -= 1
else:
    print('No tengo mas dinero')


respuesta = 's'
while respuesta == 's':
    respuesta = input("quieres seguir?? (s/n): ")
else:
    print("Gracias")

respuesta = 's'
while respuesta == 's':
    pass #para guardar el espacio para mas adelante, si aun no se que hará esta parte del codigo
print("Gracias")

nombre = input("Tu nombre: ")
for letra in nombre:
    if letra == 'r':
        break #interrumpe el codigo, si pongo federico, imprime fede
    print(letra)

nombre = input("Tu nombre: ")
for letra in nombre:
    if letra == 'r':
        continue #no interrumpe el codigo, omite la letra indicada, imprime fedeico sin la r
    print(letra)