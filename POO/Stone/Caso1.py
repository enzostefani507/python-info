class Vehiculo():
    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas

    def getColor(self):
        return self.color

    def getRuedas(self):
        return self.ruedas

class Coche(Vehiculo):
    def __init__(self,color,ruedas,velocidad,cilindrada):
        Vehiculo.__init__(self,color,ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def getVelocidad(self):
        return self.velocidad
    
    def vetCilindrada(self):
        return self.cilindrada

def main():
    c = Coche("Azul",4,100,2.5)
    print(c)

main()