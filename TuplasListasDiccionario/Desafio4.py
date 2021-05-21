especies = ("Bovino","Oso panda","Oso polar")

for animal in especies:
    print ("Hola soy {}".format(animal))

desde = int(input("Ingrese desde: "))
hasta = int(input("Ingrese hasta: "))

corta = especies[desde:hasta]

for animal in corta:
    print("Hola soy {}".format(animal))