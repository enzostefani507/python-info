cantidad_personas = int(input("Ingrese la cantidad de personas recolectoras"))
menor_a_100 = entre_100_y_200 = mayor_a_100 = 0

for i in range(cantidad_personas):
    cantidad_recolectada = int(input("Ingrese la cantidad recolectada por la persona: "+str(i+1)+"\n"))
    if cantidad_recolectada < 100:
        menor_a_100 +=1
    elif cantidad_recolectada <200:
        entre_100_y_200 +=1
    else:
        mayor_a_100 +=1

porcentaje_reco_men_a_100 = (menor_a_100/cantidad_personas)*100
porcentaje_reco_ent_100_y_200 = (entre_100_y_200/cantidad_personas)*100
porcentaje_reco_may_a_100 = (mayor_a_100/cantidad_personas)*100
print("Porcentaje personas que recolectaron menos de 100 colillas: "+str(porcentaje_reco_men_a_100)+"%")
print("Porcentaje personas que recolectaron entre 100 y 200 colillas: "+str(porcentaje_reco_ent_100_y_200)+"%")
print("Porcentaje personas que recolectaron mas de 200 colillas: "+str(porcentaje_reco_may_a_100)+"%")