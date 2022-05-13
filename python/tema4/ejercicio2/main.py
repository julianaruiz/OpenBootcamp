#Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.

#Por ejemplo: teniendo numero_inicial = 2 y numero_final = 8, el programa debe imprimir por consola: [3, 5, 7]

numero_inicial = 2
numero_final = 20

while numero_inicial <= numero_final:

    if numero_inicial % 2 != 0:
        print(numero_inicial)

    numero_inicial+=1