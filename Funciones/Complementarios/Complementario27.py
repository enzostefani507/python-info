def palabrasInversa(texto):
    palabras = texto.split()
    res = ""
    for pal in palabras:
        res = res + pal[::-1]
        res = res + " "
    return res

print(palabrasInversa("Hola mundo"))