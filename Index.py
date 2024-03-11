mi_texto = "Esta es una prueba"
resultado = mi_texto[0] #podemos probar con cualquier numero, incluso con negativos y contaria de derecha a izquierda
print(resultado)

mi_texto2 = "Esta es otra prueba"
resultado2 = mi_texto2.index("t", 5) #si ponemos un numero seguido de una coma es para indicar que a partir de ese numero empiece a buscar
#mi_texto2.index("t", 5, 10) si ponemos otra coma, buscaremos hasta el numero indicado, tener en cuenta que busca hasta un espacio antes, sin ser inclusivo.
print(resultado2) #tambien podemos buscar palabras completas y nos devolvera el numero desde donde comienza.
#mi_texto2.index("otra")
#mi_texto2.rindex("t", 5) busca de derecha a izquierda.