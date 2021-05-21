"""Ejercicio 3: Calculadora de envío

Un minorista en línea proporciona una forma de envío urgente de $ 10.95 para el primer elemento y $ 2.95 para cada
segundo elemento posterior. Escriba una función que tome el número de elementos en el pedido como su único parámetro.
Devuelva los gastos de envío del pedido como resultado de la función. Incluya un programa principal que lea la
 cantidad de artículos comprados al usuario y muestre los gastos de envío."""

base = 10.95
secundario = 2.95

def calcular_costo(elementos):
    valor = [base,base+elementos*secundario][elementos!=1]
    return valor

cantidad = int(input("Ingrese la cantidad de elementos a enviar: "))

print(calcular_costo(cantidad))