factores = ("microplastico","drogas","metales pesados")

while True:
    opcion = input("Seguir ?\nS-Si\nN-no\nSu opcion: ")
    if opcion == "S":
        eleccion = int(input("Elija un número"))
        print(factores[eleccion])
    else:
        break
