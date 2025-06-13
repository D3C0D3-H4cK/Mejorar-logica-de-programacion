# Escribe un programa que reciba un número entero y diga si es par o impar.

Numero = int(input("Escribe un número: "))

def revisarnumero(Numero):
    if Numero % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")
revisarnumero(Numero)