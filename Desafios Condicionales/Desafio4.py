recetas = {
    "Ingredientes_comunes" : ("Verduras","Berenjena"),
    "Receta1" : ("Lentejas", "Apio"),
    "Receta2" : ("Morrón", "Cebolla")
}


for key in recetas:
    print (key+ ": ")
    for elementos in recetas[key]:
        print("  -"+elementos)

eleccion_receta = input('Seleccione una receta')

eleccion_ingredientes = input("Seleccione 1 ingrediente comun")

print("La receta elegida es: ")
if eleccion_receta in recetas:
    print("- "+recetas[eleccion_receta])
if eleccion_ingredientes in recetas['Ingredientes_comunes']:
    print ("- "+eleccion_ingredientes)

