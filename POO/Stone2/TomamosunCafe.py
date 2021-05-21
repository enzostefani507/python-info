class cafetera:
    def __init__(self,capacidadM,capacidadA):
        self.capacadad_maxima = capacidadM
        self.capacidad_actual = capacidadA
    
    def setMaximo(self,maximo):
        self.__capacidadMaxima = int(maximo)

    def setActual(self,actual):
        self.__cantidadActual = int(actual)

    def getMaximo(self):
        return self.__capacidadMaxima
    
    def getActual(self):
        return self.__cantidadActual

    capacadad_maxima = property(getMaximo,setMaximo)
    capacidad_actual = property(getActual,setActual)

    def llenarCafetera(self):
        self.capacidad_actual = (self.capacadad_maxima)

    def servirTaza(self,cantidad):
        if (self.capacidad_actual - int(cantidad)) >= 0:
            self.capacidad_actual=(self.capacidad_actual - int(cantidad))
        else:
            self.vaciarCafetera

    def vaciarCafetera(self):
        self.capacidad_actual = 0

    def agregarCafe(self,cantidad):
        self.capacidad_actual = (self.capacidad_actual+int(cantidad))

c = cafetera(5,10)

print(c.getActual())
c.servirTaza(3)
print(c.getActual())
