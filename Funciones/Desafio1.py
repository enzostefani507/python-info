tipo_residuo = input("Ingese  el elemento por analizar:\n-Bolsa de plástico\n-Botella PET\n-Envase tetrabrik\n-chicle\nSu elemento es:")

def tiempo_degradacion(elemento):
    if elemento == "Bolsa de plástico":
        print ("El elemetno {} tarda en degradarse {} años".format(elemento,150))
    elif elemento == "Botella PET":
        print ("El elemetno {} tarda en degradarse {} años".format(elemento,10000))
    elif elemento == "Envase tetrabrik":
        print ("El elemetno {} tarda en degradarse {} años".format(elemento,50))
    elif elemento == "chicle":
        print ("El elemetno {} tarda en degradarse {} años".format(elemento,5))
    else:
        print("El elemento {} no encontrado".format(elemento))

tiempo_degradacion(tipo_residuo)