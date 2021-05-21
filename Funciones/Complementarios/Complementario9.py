def quitarEspacios(texto):
    palabras = texto.split()
    cad = ""
    for i in palabras:
        cad = cad + i
    return cad.isdigit

def es_entero(entrada):
    x = quitarEspacios(entrada)
    if x[0] in ['+','-']:
        x = x[1::]
    return x

def main():
    e = input("Ingrese cadena: ")
    print(es_entero(e))

main()

