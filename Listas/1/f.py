#Cargar k elementos en una cola, y luego copiarlos en una nueva lista.

datos = []

for i in range(0,5):
    valor = int(input("Ingrese un valor: "))
    datos.append(valor)

nueva_lista = []

for i in range(len(datos)):
    nueva_lista.append(datos.pop())
nueva_lista.reverse()

print(nueva_lista)