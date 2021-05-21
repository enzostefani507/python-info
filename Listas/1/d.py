l = [2,5,5,3,5,7,2,5]
numero = int(input("Ingrese un entero: "))

rep = l.count(numero)

for i in range(rep):
    l.remove(numero)

print(l)
