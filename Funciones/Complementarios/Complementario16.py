def hex2int(numeroHexa):
    valores ={
        'A' : "10",
        'B' : "11",
        'C' : "12",
        'D' : "13",
        'E' : "14",
        'F' : "15"
    }
    resultado = 0
    coef = []
    for i in numeroHexa:
        if i.isnumeric():
            coef.append(int(i))
        else:
            coef.append(int(valores[i]))
    coef.reverse()
    for i in range(len(numeroHexa)):
        resultado = resultado + coef[i]*(16**i)
    return resultado


def int2hex(decimal):
    valores ={
        "10":'A',
        "11":'B',
        "12":'C',
        "13":'D',
        "14":'E',
        "15":"F"
    }
    restos = []
    cociente = int(decimal)
    while cociente >= 1:
        r = cociente % 16
        if r >= 10:
            restos.append(str(valores[str(r)]))
        else:            
            restos.append(str(r))
        cociente = cociente // 16
    restos.reverse()
    return ''.join(restos)

def main():
    romano = input("Ingrese un hexadecimal: ")
    print("El hexadecimal en decimal es: {}".format(hex2int(romano)))

    decimal = input("Ingrese un decimal: ")
    print("El decimal en hexadecimal es: {}".format(int2hex(decimal)))

main()