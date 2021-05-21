 # Ingresar una palabra, carácter por carácter, en una lista y determinar si es palíndromo.
cad = ''
while True:
    l = input("Ingrese un caracter: ")
    if l == '':
       break
    else:
        cad = cad + l

for i in range(len(cad)):
    if cad[i] != cad[-i-1]:
        print("False")
        break
else:
    print("Verdadero")