meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']

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


def moduloCorrespondiente(mes,anio):
    nBi = (0,3,3,6,1,4,6,2,5,0,3,5)
    Bi = (0,3,4,0,2,5,0,3,6,1,4,6)
    if bisiesto(anio):
        return Bi[mes-1]
    else:
        return nBi[mes-1]


def primerDia(mes,anio):
    """
        https://es.wikibooks.org/wiki/Algoritmia/Algoritmo_para_calcular_el_d%C3%ADa_de_la_semana
        D = 0
        L = 1
        M = 2
        X = 3
        J = 4
        V = 5
        S = 6
    """
    M = moduloCorrespondiente(mes,anio)
    D = 1 #Para obtener el dia de la fech 1/mes/anio
    dia = ((anio-1)%7+((anio-1)/4-(3*((anio-1)/100+1)/4))%7+M+D%7)%7
    return round(dia)
    

def obtenerCalendario(mes,anio):
    if mes >0 and mes < 13:
        arranca = primerDia(mes,anio)
        cantidadDias = diaMes(mes,anio)
        print(f'AÑO: {anio}')
        print(f'Mes: {meses[mes-1]}')
        print(f' L  M  X  J  V  S  D')
        print(f'===================')
        d = 1
        if arranca != 1:
            cad = "   "*(arranca-1)
            print(cad,end="")
        elif arranca == 0:
            cad = "                    "
            print(cad,end="")
        while d < cantidadDias:
            for j in range(arranca,8): 
                if len(str(d)) == 1:
                    print(" "+str(d),end = " ")
                else:
                    print(d,end =" ")
                if d == cantidadDias:
                    break
                d += 1
            arranca = 1
            print("")
    else:
        return 'No valido'

obtenerCalendario(4,2020)
