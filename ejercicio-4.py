numero = int(input("Ingrese un numero positivo "))

if numero > 0:
    suma = numero * (numero + 1 ) // 2

    print(f"El resultado es: {suma}")
else:
    print("El numero dijitado no es un entero positivo")