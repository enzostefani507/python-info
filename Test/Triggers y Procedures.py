def sumar(x,y):
    return x+y

def restar(x,y):
    return x-y

def multiplicar(x,y):
    return x*y

def dividir(x,y):
    if y == 0:
        raise ValueError("no se puede div por cero")
    else:
        return x/y