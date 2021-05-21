def capitalizar(texto):
    palabras = texto.split()
    resultado = list()
    for pal in palabras:
        if pal[0] in ["¡","¿"] and len(pal)>=2:
            resultado.append(pal[0] + pal[1].upper() + pal[2:].lower())
        else:
            if ult in [".","!","?"]:
                resultado.append(pal[0] + pal[1].upper() + pal[2:].lower())
            else:
                resultado.append(pal.lower())
        ult = pal[-1]
    texto = ""
    for i in range(len(resultado)-1):
        texto = texto + resultado[i] + " "
    texto[len(texto)]=""
    return texto

x= capitalizar("¿a qué hora tengo que estar allí? ¿cuál es la dirección?")
texto_esperado = "¿A qué hora tengo que estar allí? ¿Cuál es la dirección?"
print(x)
print(x==texto_esperado)