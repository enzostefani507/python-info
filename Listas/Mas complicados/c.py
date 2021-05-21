import random
#c. Simular la operación de colas de un Rapipago, que funciona con dos colas diferentes. 
# El usuario llega y se ubica en la cola de menor cantidad de personas. 
# Al finalizar el proceso indique cuántos elementos tiene cada cola.

#Defino el estado inicial aleatoriamente
cola1 = list(range(random.randrange(10)))
cola2 = list(range(random.randrange(10)))
i = 1

def estado_cola():
    print("Estado actual:\nCola 1:{} personas \nCola 2:{} personas\n".format(len(cola1),len(cola2)))

estado_cola()

while True: 
    estado_cola()
    print("Ingreso la persona {}".format(i))
    if len(cola2)<=len(cola1):
        mensaje = "Se ubica en la cola 2"
        cola2.append(i)
    else:
        mensaje = "Se ubica en la cola 1"
        cola1.append(i)
    print("La persona {} {}".format(i,mensaje))
    estado_cola()
    if input("Ingrese S para que ingrese la siguiente persona: ") == "S":
        i += 1
        continue
    else:
        estado_cola()
        break
