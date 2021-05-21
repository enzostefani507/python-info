#Elabore un programa que dada una lista de 15 elementos, copie en otra lista los elementos pares multiplicados por 2.
lista = list(range(15))

otra_lista = []

for i in lista:
    if i % 2 == 0 :
        otra_lista.append(i*2)

print(lista)
print(otra_lista)