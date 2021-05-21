class Pila:
    def __init__(self,limite):
        self.__limite = limite
        self.__lista = []

    def cantidad_elementos(self):
        return len(self.__lista)

    def agregar_elemento(self, elem):
        if self.__limite > self.cantidad_elementos():
            self.__lista.append(elem)
            return True
        else:
            return False

    def quitar_elemento(self):
        if self.cantidad_elementos > 0:
            return self.__lista.pop()

class Cola:
    def __init__(self,limite):
        self.__limite = limite
        self.__lista = []

    def cantidad_elementos(self):
        return len(self.__lista)

    def agregar_elemento(self, elem):
        if self.__limite > self.cantidad_elementos():
            self.__lista.append(elem)
            return True
        else:
            return False

    def quitar_elemento(self):
        if self.cantidad_elementos > 0:
            return self.__lista.pop(0)