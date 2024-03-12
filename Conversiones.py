num1 = 20
num2 = 30.5


num1 = num1 + num2 #conversion implicita
print(type(num1))
print(type(num2))

num3 = 5.8
print(num3)
print(type(num3))

num4 = int(num3) #conversion explicita, elimina los decimales
print(num4)
print(type(num4))

edad = input("Dime tu edad: ")
print(type(edad))
edad = int(edad) #aqui cambiamos un string a un integer
print(type(edad))
nueva_edad = 1 + edad
print(nueva_edad)