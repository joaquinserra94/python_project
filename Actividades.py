print("#----------------------------------------------")
print("ejercicio 1")

import random

def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2

def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2

    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif 6 < suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

# Lanzar los dados
dado1, dado2 = lanzar_dados()

# Evaluar la jugada
resultado_jugada = evaluar_jugada(dado1, dado2)
print(resultado_jugada)

#-----------------------------------------------------------------
print("#----------------------------------------------")
print("ejercicio 2")
def reducir_lista(lista):
    # Eliminar duplicados y el valor más alto
    lista_sin_duplicados = list(set(lista))
    maximo = max(lista_sin_duplicados)
    lista_sin_duplicados.remove(maximo)
    return lista_sin_duplicados

def promedio(lista):
    # Calcular el promedio de los valores en la lista
    if len(lista) == 0:
        return 0
    else:
        return sum(lista) / len(lista)

# Ejemplo de uso
lista_numeros = [1, 2, 15, 7, 2]
lista_reducida = reducir_lista(lista_numeros)
resultado_promedio = promedio(lista_reducida)
print(lista_reducida)  # Salida: [1, 2, 7]
print(resultado_promedio)  # Salida: 3.3333333333333335

#----------------------------------------------
print("#----------------------------------------------")
print("ejercicio 3")
import random

def lanzar_moneda():
    resultado = random.choice(["Cara", "Cruz"])
    return resultado

def probar_suerte(resultado_moneda, lista_numeros):
    if resultado_moneda == "Cara":
        print("La lista se autodestruirá")
        return []
    else:
        print("La lista fue salvada")
        return lista_numeros

# Ejemplo de uso
lista_numeros = [1, 2, 3, 4, 5]
resultado_moneda = lanzar_moneda()
lista_resultante = probar_suerte(resultado_moneda, lista_numeros)

print("Resultado del lanzamiento de la moneda:", resultado_moneda)
print("Lista resultante:", lista_resultante)

