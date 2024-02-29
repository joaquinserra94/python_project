texto = "Este es el texto de Joaquin"
resultado = texto.upper()
print(resultado)

texto = "Este es el texto de Joaquin"
resultado = texto[2].upper() #pasa todo a mayuscula
print(resultado)

texto = "Este es el texto de Joaquin"
resultado = texto.lower() # pasa todo a minusculas
print(resultado)

texto = "Este es el texto de Joaquin"
resultado = texto.split() #Lo separa en elementos y lo convierte en lista
print(resultado)

texto = "Este es el texto de Joaquin"
resultado = texto.split("t")
print(resultado)

a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a,b,c,d]) #desde la variable que contiene al espacio, creamos una lista y unimos todo con join
print(e)

texto = "Este es el texto de Joaquin"
resultado = texto.find("t")
print(resultado)

texto = "Este es el texto de Joaquin"
resultado = texto.replace("Joaquin","todos")
print(resultado)