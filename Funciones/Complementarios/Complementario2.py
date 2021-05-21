"""Ejercicio 2: Tarifa del taxi
En una jurisdicción particular, las tarifas de taxi consisten en una tarifa base de $40.00, 
más $15.00 por cada 140 metros recorridos. Escriba una función que tome la distancia recorrida 
(en kilómetros) como su único parámetro y devuelva la tarifa total como su único resultado. 
Escriba un programa principal que use la función.
Sugerencia: Utilice constantes para presentar la base y la porción variable de las tarifas 
así el programa podrá actualizar fácilmente cuando las tasas aumentan."""

tarifa = 15
base=40

def km_a_m(numero):
    return numero*1000

def calculo_tarifa(distancia):
    #distancia en km
    return base + (km_a_m(distancia)/140)


recorrido = int(input("Ingrese la distancia recorrida en Km: "))
print("La tarifa total es {}".format(calculo_tarifa(recorrido)))