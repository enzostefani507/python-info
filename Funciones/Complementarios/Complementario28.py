def elementos_impares(lista):
    res = []
    for i in range(len(lista)):
        if i % 2 != 0:
            res.append(lista[i])
    return res

print(elementos_impares([1, 2, 3, 4]))