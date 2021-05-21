while True:
    print("->Precione Ctr+C para terminar el programa <-")
    total = int(input("Ingrese total a pagar: "))
    codigo_descuento = input("Ingrese el codigo de descuento:  \n Rojo -40 % Descuento \n Rojo -25 % Amarillo \n Blanco -0% Descuento\n ->")
    codigo_descuento = codigo_descuento.lower()
    if codigo_descuento == "rojo":
        descuentos = 0.40
    elif codigo_descuento =="amarillo":
        descuento = 0.25
    else:
        descuento = 0
    abonar = total - (total * descuento)
    print("Usted debe abonar: " + str(abonar))    