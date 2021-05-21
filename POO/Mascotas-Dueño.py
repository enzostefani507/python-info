class Mascota:
    def __init__(self,nombre,color,peso):
        self.nombre = nombre
        self.color = color
        self.peso = peso
    
    def getNombre(self):
        return self.nombre
    
    def getPeso(self):
        return self.peso

    def getColor(self):
        return self.color

    def nombre_color(self):
        return "\n Nombre: "+self.getNombre() +"\n Color: "+self.getColor()

class Dueño:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.adopta = []

    def nombreCompleto(self):
        return self.apellido+" "+self.nombre

    def adoptar(self,mascota):
        self.adopta.append(mascota)

    def adopcion(self):
        print("Nombre    | Peso     |Color")
        for i in self.adopta:
            print(f'{i.getNombre()} | {i.getPeso()} |  {i.getColor()}')
            #ver .center

    def obtenerMascotas(self):
        mascotas = []
        for mascota in self.adopta:
            dic = {}
            dic["Nombre"] = mascota.getNombre()
            dic["Color"] = mascota.getColor() 
            mascotas.append(dic)
        return tuple(mascotas)

p1 = Dueño("Enzo","Benites")

m1 = Mascota("Toti","Gris",15)
m2 = Mascota("Chich","Blanco",15)
m3 = Mascota("aas","Marron",15)

p1.adoptar(m1)
p1.adoptar(m2)
p1.adoptar(m3)

p1.adopcion()

print(p1.obtenerMascotas())