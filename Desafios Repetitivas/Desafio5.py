import random
import string

patente = ""
vehiculos_tira_basura = 0
ya_multados = 0
vehiculos_observados = 0

for k in range(random.randint(1000,100000)): #En este segmento de codigo me encargo de generar registros sobre los que trabajar
    for i in range(3): 
        patente = patente + random.choice(string.ascii_uppercase)
    for i in range(3):
        patente = patente + str(random.randint(0,9))
    control = patente + str(random.randint(0,1)) + str(random.randint(0,1))
    vehiculos_observados +=1
    if control[6] == "1":
        vehiculos_tira_basura +=1 
        if control[7] == "1":
            ya_multados += 1
    patente = ""
print("Se observaron "+str(vehiculos_observados)+" vehiculos")
print("Los vehiculos que tiraron basura: "+str(vehiculos_tira_basura))
if ya_multados == 0:
    print("El porcentaje de los vehiculos que tiraron basura y previamente fueron multados: 0 %")
else:
    print("El porcentaje de los vehiculos que tiraron basura y previamente fueron multados: "+str(format((vehiculos_tira_basura/ya_multados), '.2f'))+" %")