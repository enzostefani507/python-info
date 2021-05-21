#Escriba un algoritmo que permita cargar una lista. Y que luego, una vez cargada, controle y sustituya cualquier elemento negativo por 0.
datos = []
while True:
    i = input("Ingrese cualquier caracter para interrumpir\nIngrese un numero para continuar: ")
    print("-------------------------")
    if i.lstrip('-').isdigit() ==  True:
        datos.append(i)
    else:
        correcto = []
        for i in datos:
            num = int(i)
            if num >= 0 :
                correcto.append(num)
            else:
                correcto.append(0)
        break
print(correcto)

    