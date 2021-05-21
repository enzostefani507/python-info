def centrar(text,ancho):
    lados = ancho//2
    relleno = " "*lados
    return relleno+text+relleno

def main():
    entrada = input("Ingrese texto: ")
    margenes = int(input("Centrar: "))
    print(centrar(entrada,margenes))

main()
