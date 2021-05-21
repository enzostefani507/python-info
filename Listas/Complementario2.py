#b. Leer una frase y luego invierta el orden de las palabras en la frase. 

texto = input("Ingrese un texto: ")
palabras = texto.split()
for i in palabras[::-1]:
    print(i,end=" ")