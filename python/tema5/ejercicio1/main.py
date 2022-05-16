#Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como
# parámetros y otra función que calcule el área de un círculo recibiendo el radio del mismo.

import math

print("Area de un triangulo")
altura = int(input("Ingrese la altura: "))
base = int(input("Ingrese la base: "))

triangulo = lambda altura, base: (base * altura) / 2

print(triangulo(altura, base))

print("\n")
print("Area de un circulo")

radio = float(input("Ingrese el radio: "))

circulo = lambda radio: math.pi * (radio**2)

print(circulo(radio))

