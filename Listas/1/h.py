#Construya un algoritmo que sume todos los elementos en posición par de una lista.

lista = [1,4,6,2,4,6]
res = 0

for i in range(len(lista)):
    if i % 2 == 0:
        res += lista[i]

print(res)