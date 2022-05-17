#Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.


def bisiesto(anio):

    if anio % 4 == 0:
        if anio % 100 == 0:
            if anio % 400 == 0:
                print("Es bisiesto")
            else:
                print("No es bisiesto")
        else:
            print("Es bisiesto")
    else:
        print("No es bisiesto")

anio = int(input("Ingrese un año "))

bisiesto(anio)