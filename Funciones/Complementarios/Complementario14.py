import random

def generarMatricula():
    numero = random.randint(0,9999)
    letras = chr(random.randint(65,90))+chr(random.randint(65,90))+chr(random.randint(65,90))
    patente = str(numero)+letras
    return patente

def main():
    generado = generarMatricula()
    print(generado)

main()