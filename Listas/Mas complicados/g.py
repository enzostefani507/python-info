#Se tiene una lista que almacena pedidos en orden de llegada,
#por ende puede haber más de un pedido para el mismo artículo. 
#Crear una lista donde se almacene la cantidad de pedidos por artículo.

pedidos = [1,2,4,6,2,1,5,7,1,3,6,1,2]
solo_articulos = []
cantidad_por_articulo = []

for i in pedidos:
    if i not in solo_articulos:
        solo_articulos.append(i)

for i in solo_articulos:
    cantidad_por_articulo.append([i,pedidos.count(i)])

print(cantidad_por_articulo)