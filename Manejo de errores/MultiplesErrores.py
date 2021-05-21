try:
    n = float(input("Introduce un número divisor: "))
    5/n
except TypeError: #Preguntar cual es la diferencia con Value Error
    print("No se puede dividir el número entre una cadena")

except ValueError:
    print("Debe introducir una cadena que sea un numero")

except ZeroDivisionError:
    print("No se puede dividir por cero, prueba otro número")

except Exception as e:
    print("Ha ocurrido un error no previso",type(e).__name__)