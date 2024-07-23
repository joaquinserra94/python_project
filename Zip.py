nombres = ['Ana','Hugo','Valeria']
edades = [65,29,42]
ciudades = ['Lima','Madrid','Mexico']
combinados = list(zip(nombres,edades,ciudades))

for nombres,edades,ciudades in combinados:
    print(f'{nombres} tiene {edades} años y vive en {ciudades}')


# Lista de números en español
numeros_espanol = ["uno", "dos", "tres", "cuatro", "cinco"]

# Lista de números en portugués
numeros_portugues = ["um", "dois", "três", "quatro", "cinco"]

# Lista de números en inglés
numeros_ingles = ["one", "two", "three", "four", "five"]

# Crear el zip con las traducciones
numeros_zip = zip(numeros_espanol, numeros_portugues, numeros_ingles)

# Convertir el objeto zip en una lista
numeros = list(numeros_zip)

# Imprimir el resultado
print(numeros)
