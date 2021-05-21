def precedencia(entrada):
    if '^' in entrada:
        return 3
    elif '*' in entrada:
        return 2
    elif '+' in entrada or  '-' in entrada:
        return 1
    else:
        return -1

def main():
    e = input("Ingrese las operaciones: ")
    print(precedencia(e))

main()