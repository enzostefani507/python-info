def verificarContraseña(pwd):
    return len(pwd)>=8 and verificarMinimoMayuscula(pwd) and verificarMinimoMinuscula(pwd) and verificarMinimoNumeros(pwd)

def verificarMinimoMayuscula(pwd):
    for i in pwd:
        if i.isupper():
            return True
    return False

def verificarMinimoMinuscula(pwd):
    for i in pwd:
        if i.islower():
            return True
    return False

def verificarMinimoNumeros(pwd):
    for i in pwd:
        if i.isnumeric():
            return True
    return False

def main():
    contraseña = input("Ingrese su contraseña")
    verif = verificarContraseña(contraseña)
    print("La firmacion: Su contraseña es segura es {}".format(verif))

main()