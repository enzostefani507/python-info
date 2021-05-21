def relacion(a = None,b = None):
    if a == None or b == None:
        print ("Debe ingresar ambos valores")
        return
    if a > b:
        print("Nombre ciudad 1")
    elif a < b:
        print("Nombre ciudad 2")
    else:
        print("Ciudades 1 y 2")

relacion(100,500)