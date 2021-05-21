while True:
    try:
        n = float(input("Introduce un numero: "))
        m = 2
        print("{}/{}={}".format(n,m,n/m))
    except:
        print("Ha ocurrido un eror, introduce bien el numero")
    else:
        print("Todo perfecto")
        break
    finally:
        print("Cerrando el programa")