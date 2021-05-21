#Leer una frase y luego invierta el orden de las palabras en la frase. 
#Por Ejemplo: “una imagen vale por mil palabras” debe convertirse en “palabras mil por vale imagen una”.

frase = input("Ingrese una frase: ")
palabras = frase.split()
palabras.reverse()
respuesta = " ".join(palabras)
print(respuesta)
