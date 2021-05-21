def  convertir(b1,b2,numero):
    if b1 > 16 or b1 < 2 or b2 > 16 or b2 < 2:
        print("Bases no validas")
    else:
        if b2 == 10:
            return nABase10(b1,numero)
        elif b1 == 10:
            return diezABaseN(b2,numero)
        else:
            paraCambio = nABase10(b1,numero)
            return diezABaseN(b2,paraCambio)
        

def nABase10(b,numero):
    valores ={
        'A' : "10",
        'B' : "11",
        'C' : "12",
        'D' : "13",
        'E' : "14",
        'F' : "15"
    }
    conv = 0
    num = numero[::-1]
    for i in range(len(num)):
        if num[i].isnumeric():
            conv = conv + int(num[i])*(b**i)
        else:
            conv = conv + int(valores[num[i].upper()])*(b**i)
    return conv


def diezABaseN(b,numero):
    valores2 ={
        '10' : "A",
        '11' : "B",
        '12' : "C",
        '13' : "D",
        '14' : "E",
        '15' : "F"
    }
    coc = int(numero)
    res = []
    conv = ""
    while coc >= 1:
        r = coc % b
        if r >= 10:
            r = valores2[str(r)]
        res.append(r)
        coc = coc // b
    for i in res:
        conv = str(i)+ conv
    return conv


def main():
    b1 = int(input("Ingrese la base orgien: "))
    b2 = int(input("Ingrese la base destino: "))
    numero = input("Ingrese el numero a convertir: ")
    print(convertir(b1,b2,numero))

main()