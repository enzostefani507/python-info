#Cargar m elementos en una pila, y luego copiarlos en una nueva lista.
datos = []

for i in range(0,5):
    valor = int(input("Ingrese un valor: "))
    datos.insert(0,valor)

nueva_lista = []

for i in range(len(datos)):
    nueva_lista.append(datos.pop())

print(nueva_lista)