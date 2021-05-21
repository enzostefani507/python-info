conocimiento = list()
while True:
    res = int(input("Ingrese cuanto conoce sobre contaminacion: "))
    conocimiento.append(res)
    seguir = input("S-SI\nN-No\n>>")
    if seguir != "S":
        break
conocimiento.sort()
print(conocimiento)