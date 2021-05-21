cientificos = dict()

while True:
    opcion = input ("¿Seguir cargando?\nS-si\nN-no\nSu opcion: ")
    if opcion == "S":
        nombre = input("Ingrese nombre del cientifico: ")
        correo = input("Ingrese correo del cientifico: ")
        """cientificos.setdefault(nombre,correo)"""
        cientificos[nombre] = correo
    elif opcion == "N":
        break

for nombre,correo in cientificos.items():
    print("El correo electronico de {} es {}".format(nombre,correo))