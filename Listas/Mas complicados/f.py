#Se tiene una lista con los datos de los clientes de una compañía de telefonía celular,
#  los cuales pueden aparecer repetidos en la lista, si tienen registrado más de un número telefónico. 
# La compañía para su próximo aniversario desea enviar un regalo a sus clientes,
#  sin repetir regalos a un mismo cliente. En una lista se almacenan los regalos disponibles en orden. 
# Se desea un programa que cree una nueva lista con los clientes, sin repetir y ordenada. 
# Y que al final muestre el regalo que le corresponde a cada cliente.

clientes = [1,2,2,5,6,7,5]

regalos = ['regalo1','regalo2','regalo3']

clientes_unico = list()

for i in clientes:
    if clientes_unico.count(i) == 0:
        clientes_unico.append(i)

clientes_unico.sort()

j = 0
for i in clientes_unico:
    print(f'{i}:{regalos[j%len(regalos)]}')
    j += 1