def sumar_rango(a,b):
    res = 0
    for i in range(a,b+1):
        res = res + i
    return res

print(sumar_rango(3,6))