"""Ejercicio 4: Mediana de tres valores
Escriba una función que tome tres números como parámetros y devuelva el valor medio de esos parámetros como resultado. 
Incluya un programa principal que lea tres valores del usuario y muestre su mediana.
Sugerencia: El valor medio es el medio de los tres valores cuando se ordenan en orden ascendente. 
Se puede encontrar usando declaraciones if, o con un poco de creatividad matemática."""

def mediana(*argv):
    datos = list(argv)
    datos.sort()
    if len(datos)%2 != 0:
        mediana = datos[len(datos)//2]
    else:
        mediana = datos[len(datos)//2]+datos[(len(datos)//2)-1]
        mediana = mediana / 21
    return mediana

valor1 = int(input("Ingrese un valor: "))
valor2 = int(input("Ingrese otro valor: "))
valor3 = int(input("Ingrese otro valor: "))

print("La media de los valores {},{},{} es {}".format(valor1,valor2,valor3,mediana(valor1,valor2,valor3)))