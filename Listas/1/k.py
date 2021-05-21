#Cargue dos listas, y actualice la primer lista con los elementos que están en la segunda y no en la primera.

lista_1 = [23,3,5,2,3]
lista_2 = [23,5,3,8,9]

for i in lista_2:
    if i not in lista_1:
        lista_1.append(i)
    
print(lista_1)