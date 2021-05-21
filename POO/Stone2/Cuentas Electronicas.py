class persona:
    def __init__(self,nombre):
        self.nombre = nombre

class cuenta:
    def __init__(self,persona,cantidad=None):
        self.titular = persona
        if cantidad < 0:
            pass
        else:
            self.cantidad = cantidad
    
    def ingrearCantidad(self,cantidad):
        if cantidad < 0:
            pass
        else:
            self.cantidad = cantidad

    def mostrar(self):
        print(self.__dict__)
    
    def retirar(self,retira):
        self.cantidad = self.cantidad - retira