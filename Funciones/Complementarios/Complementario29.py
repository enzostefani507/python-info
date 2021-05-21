def convertir_a_binario(numero):
    coc = int(numero)
    res = []
    conv = ""
    while coc >= 1:
        r = coc % 2
        res.append(r)
        coc = coc // 2
    for i in res:
        conv = str(i)+ conv
    return str(conv)

def convertir_a_decimal(numero):
    res = 0
    trato = numero[::-1]
    for i in range(len(numero)):
        res = res + int(trato[i])*(2**i)
    return res