def trianguloValido(a,b,c):
    datos = [a,b,c]
    mayor_lado = max(datos)
    posicion_mayor_dato = datos.index(mayor_lado)
    mayor = datos.pop(posicion_mayor_dato)
    return mayor <= (datos[0]+datos[1])

c1 = int(input("Ingrese lado"))
c2 = int(input("Ingrese lado"))
c3 = int(input("Ingrese lado"))
print(trianguloValido(c1,c2,c3))