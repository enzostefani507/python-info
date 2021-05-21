def descomponer(numero):
    #Funcion retorna mil,centa,decena y unidades
    mil = numero // 1000
    cen = (numero - mil * 1000)//100
    dec = (numero -(mil * 1000 + cen *100))//10
    uni = numero - (mil * 1000 + cen * 100 + dec *10)
    return mil,cen,dec,uni


def unidad(n):
    if n <= 3:
        return "I"*n
    elif n == 4:
        return "IV"
    elif n <= 8:
        return "V"+"I"*(n-5)
    else:
        return "IX"


def decena(n):
    if n <= 3:
        return "X"*n
    elif n == 4:
        return "XL"
    elif n <= 8:
        return "L"+"X"*(n-5)
    else:
        return "XC"


def centena(n):
    if n <= 3:
        return "C"*n
    elif n == 4:
        return "D"
    elif n <= 8:
        return "D"+"C"*(n-5)
    else: 
        return "CM"


def miles(n):
    if n <= 3:
        return "M"*n


def convertir_Romano(numero):
    if numero >= 1 and numero <= 3000:
        m,c,d,u = descomponer(numero)
        resultado = miles(m)+centena(c)+decena(d)+unidad(u)
        return resultado
    else:
        print("Numero {} fuera de rango".format(numero))


def main():
    conv = int(input("Ingrese un numro: "))
    conv_romano = convertir_Romano(conv)
    print("El numero {} en romano es {}".format(conv, conv_romano))


main()