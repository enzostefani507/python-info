while True:
    try:
        n = float(input("Introduce un divisor: "))
        m = 2
        print("{}/{}={}".format(n,m,n/m))
        break
    except:
        print("Ha ocurrido un eror, introduce bien el numero")
        