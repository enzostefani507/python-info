def primo(numero):
    if numero >= 1:
        for i in range(2,numero):
            if (numero % i ) == 0:
                return False
        return True
    else:
        return False

def proximo_primo(num):
    probar = num + 1
    while True:
        if primo(probar):
            return probar
        else:
            probar += 1

numero = int(input("Ingrese un numero: "))
print("El proximo primo es: {}".format(proximo_primo(numero)))