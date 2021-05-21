#a. Ingresar una palabra, carácter por carácter, en una lista y determinar si es palíndromo.
def afirmar_algo(veracidad,algo):
    v=["falso","verdadero"][veracidad == True]
    print("{} es {}".format(algo,v))

palabra = ""

while True:
    caracter = input("Ingrese un caracter: ")
    palabra = [palabra+caracter,palabra ][caracter in [""," "]]
    if caracter in [""," "]:
        palabra=palabra.lower()
        afirmar_algo(palabra == palabra[::-1],"La afirmacion: Palabra <{}> es palindromo".format(palabra))
        break