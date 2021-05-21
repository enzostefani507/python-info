from colorama import init, Back
init()

fila = int(input("Ingrese numero de filas: "))
columnas = int(input("Ingrese numero de columnas: "))

cambiar_columna = True
for i in range(1,fila+1):
    for j in range(1,columnas+1):
        if cambiar_columna:
            print(Back.GREEN+"  ",end="")
            cambiar_columna = False
        else:
            print(Back.WHITE+"  ",end="")
            cambiar_columna = True
        if (j == columnas) and i%2 != 0:
            cambiar_columna = False
        elif (j == columnas) and i%2 == 0:
            cambiar_columna = True
    print("")