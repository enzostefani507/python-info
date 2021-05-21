#Cargar dos listas con la misma cantidad de elementos. Luego mezclarlas, cargándolas ordenadas en otra lista.
lista_1 = list(range(0,5,2))
lista_2 = list(range(2,10,3))

mezcla = lista_1.copy()
mezcla.extend(lista_2)

mezcla.sort()

print(f'Lista 1: {lista_1}')
print(f'Lista 2: {lista_2}')
print(f'Mezcla: {mezcla}')
