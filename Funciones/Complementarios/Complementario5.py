def ordinal(numero):
    ordinales = {
        1 : "primero",
        2 : "segundo",
        3 : "tercero",
        4 : "cuarto",
        5 : "quinto",
        6 : "sexto",
        7 : "septimo",
        8 : "octavo",
        9 : "noveno",
        10: "decimo",
        11: "undecimo",
        12: "duodeciomo"
    }
    if numero > 12 or numero <= 0:
        return ""
    else:
        return ordinales[numero]

print("Es el {}".format(ordinal(1)))