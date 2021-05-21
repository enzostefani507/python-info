
def diaMes(mes,anio):
    correspone = {
        1:31,
        2:28,
        3:31,
        4:30,
        5:31,
        6:30,
        7:31,
        8:30,
        9:31,
        10:31,
        11:30,
        12:31
    }
    if mes == 2 and bisiesto(anio):
        return correspone[2]+1
    else:
        return correspone[mes]

def bisiesto(anio):
    return anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0
    
    

def main():
    mes = int(input("Ingrese un mes: "))
    anio = int(input("Ingrese un año: "))
    print("El mes {} tiene {} dias".format(mes,diaMes(mes,anio)))

main()