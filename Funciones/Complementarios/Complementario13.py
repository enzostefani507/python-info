import random

def generarContraseña():
    contraseña = ""
    longitud = random.randint(7,10)
    for i in range(longitud):
        valorASCII = random.randint(33,126)
        contraseña = contraseña + chr(valorASCII)
    return contraseña

def main():
    pwd = generarContraseña()
    print(pwd)

main()