#Haz un programa que almacene 5 elementos en una variable del tipo lista, la modiﬁque para que cada componente sea igual al cuadrado del componente original. El programa mostrara la lista resultante por pantalla.
datos = []
resultados = []

for i in range(5):
    x = input("Ingrese elemento: ")
    datos.append(x)

for i in datos:
    resultados.append(int(i)**2)

print(resultados)