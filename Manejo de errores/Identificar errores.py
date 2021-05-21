try:
    n = input("Introduce un número: ")
    5/n
except Exception as e: #Guardamos la excepción en e
    print("Ha ocurrido un error =>", type(e).__name__)