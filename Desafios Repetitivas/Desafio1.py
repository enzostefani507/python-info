cuentas = {
    "Enzo": "1234",
    "Brisa": "1234",
    "Marta": "1234"
    }
numero_de_intentos = 3

print("Programa item a")
while True:
    usuario = input("Ingrese su ususario: ")
    if usuario in cuentas:
        break
    else:
        print("Usuario incorrecto")

while True:
    contrasena = input("Ingrese su contraseña: ")
    if cuentas[usuario] != contrasena:
        print("Contraseña incorrecta")
    else:    
        print("Exito")
        break
        
print("Programa item b")
"""Considero que el numero de intentos se aplican solo a las contraseñas"""
while True: 
    usuario = input("Ingrese su ususario: ")
    if usuario in cuentas:
        break
    else:
        print("Usuario incorrecto")

for i in range(1, numero_de_intentos+1):
    contrasena = input("Ingrese su contraseña: ")
    if (cuentas[usuario] != contrasena):
        if (numero_de_intentos!=i):
            print("Contraseña invalida, quedan "+str(numero_de_intentos-i)+" intentos")
        else:
            print("Numero de intentos agotados")
    else:    
        print("Exito")
        break
    