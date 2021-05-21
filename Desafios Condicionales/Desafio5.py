nombre_de_barrio = input("Ingrese el nombre del barrio: ")
nombre_de_barrio = nombre_de_barrio.upper()

ubicacion = input("Ingrese la ubicación: \n 'C': Centrico\n 'NC':No centrico\n ")
ubicacion = ubicacion.upper()

if (ubicacion == "C") and (nombre_de_barrio[0] < "M"):
    seccion = "A"
elif (ubicacion == "NC") and (nombre_de_barrio[0] > "M"):
    seccion = "A"
else:
    seccion = "B"

print("Usted se encuentra en la seccion: "+seccion)