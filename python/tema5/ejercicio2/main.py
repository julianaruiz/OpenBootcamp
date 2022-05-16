#Escribe una función que pueda decirte si un número (número entero) es primo o no.

numero = int(input("Ingrese un numero: "))

def primo(numero, n=2):
    if n >= numero:
        print("Es primo")
        return True
    elif numero % n != 0:
        return primo(numero, n + 1)
    else:
        print("No es primo", n, "es divisor")
        return False

primo(numero)