import math
"""Ejercicio 1: Triángulos
Escriba una función que tome las longitudes de los dos lados más cortos de un triángulo rectángulo 
como sus parámetros y devuelva la hipotenusa del triángulo, calculada usando el teorema de Pitágoras, 
como resultado de la función. Incluya un programa principal que lea las longitudes de los lados más 
cortos de un triángulo rectángulo del usuario, use su función para calcular la longitud de la hipotenusa 
y muestre el resultado."""

def pitagoras(c1,c2):
    hipotenusa = math.sqrt(c1*c1+c2*c2)
    return hipotenusa

lado1 = int(input("Ingrese uno de los lados cortos: "))
lado2 = int(input("Ingrese otro de los lados cortos: "))

print(pitagoras(lado1,lado2))
