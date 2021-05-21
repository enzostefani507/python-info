def separar(*args):
    mayor_a_100 = []
    menor_a_100 = []
    for ciudad in args:
        if ciudad[1]>100:
            mayor_a_100.append(ciudad)
        else:
            menor_a_100.append(ciudad)
    mayor_a_100 = sorted(mayor_a_100,key=lambda numero: numero[1])
    menor_a_100 = sorted(menor_a_100,key=lambda numero: numero[1])
    return mayor_a_100,menor_a_100


res = separar(["Resistencia",5312],["Las palmas",39],["Bararnqueras",321],["Villa",159])
print ("Las ciudades que plantaron mas de 100 arboles son: ")
for i  in res[0]:
    print (i[0]+" - "+str(i[1]))
print ("Las ciudades que plantaron menos de 100 arboles son: ")
for i  in res[1]:
    print (i[0]+" - "+str(i[1]))