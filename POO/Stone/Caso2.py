class vehiculo:
    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas
    def categoria(self):
        return type(self).__name__

class coche(vehiculo):
    def __init__(self,color,ruedas,velocidad,cilindrada):
        super().__init__(color,ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

class bicicleta(vehiculo):
    def __init__(self,color,ruedas,tipo):
        super().__init__(color,ruedas)
        self.tipo = tipo

class camioneta(coche):
    def __init__(self,color,ruedas,velocidad,cilindrada,carga):
        super().__init__(color,ruedas,velocidad,cilindrada)
        self.carga = carga

class motocicleta(bicicleta):
    def __init__(self,color,ruedas,tipo,velocidad,cilindrada):
        super().__init__(color,ruedas,tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

def catalogar(vehiculos):
    cantidad = 1
    for i in vehiculos:
        caracteristicas = i.__dict__
        print("====== Vehiculo {}======".format(cantidad))
        cantidad += 1
        print(">>Tipo : {} ".format(type(i).__name__))
        for j in caracteristicas.items():
            print(">>{} : {} ".format(j[0],j[1]))
        print("_______________________")
        

def catalogar2(vehiculos,ruedas=None):
    seleccionados = []
    if ruedas == None:
        catalogar(vehiculos)
    else :
        for i in vehiculos:
            if i.ruedas == ruedas:
                seleccionados.append(i)
        print("Se ha encontrado {} vehiculos con {} ruedas".format(len(seleccionados),ruedas))
        catalogar2(seleccionados)


def main():
    vehiculos = []
    v1 = bicicleta("Rojo",2,"urbana")
    v2 = bicicleta("Rojo",2,"urbana")
    v3 = coche("Verde",4,100,1.5)
    v4 = camioneta("Azul",8,150,1.5,500)
    v5 = motocicleta("rosa",2,50,0.5,"urbana")
    vehiculos.append(v1)
    vehiculos.append(v2)
    vehiculos.append(v3)
    vehiculos.append(v4)
    vehiculos.append(v5)
    #catalogar(vehiculos)
    catalogar2(vehiculos,4)

main()