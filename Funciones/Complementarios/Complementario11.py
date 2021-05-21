def primo(numero):
    if numero >= 1:
        for i in range(2,numero):
            if (numero % i ) == 0:
                return False
        return True
    else:
        return False

numero = int(input("Ingrese un numero: "))
print(primo(numero))