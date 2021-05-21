class producto:
    def __init__(self,identificador,precio):
        self.__identificador = identificador
        self.__precio = precio

    def getId(self):
        return self.__identificador

    def getPrecio(self):
        return self.__precio

class bebidas(producto):
    def __init__(self,identificador,precio,litros,marca):
        producto.__init__(self,identificador,precio)
        self.litros = litros
        self.marca = marca

class aguaMineral(bebidas):
    def __init__(self,identificador,precio,litros,marca,origen):
        bebidas.__init__(self,identificador,precio,litros,marca)
        self.origen = origen

class gaseosa(bebidas):
    def __init__(self,porcentajeAzucar):
        self.porcentajeAzucar = porcentajeAzucar
    
    def setPromocion(self,promo):
        self.promocion = promo

    def getPrecio(self):
        if self.promocion != None:
            return self.__precio*0.90
        else:
            return self.__precio

class almacen:
    def __init__(self):
        self.productos = {}
    
    def agregarProducto(self,producto):
        if producto.getId not in self.productos.keys():
            self.productos[producto.getId] = producto
        else:
            print ('No se agrego el producto, id repetido')

    def eliminarProducto(self,identificador):
        if producto.getId not in self.productos.keys():
            del self.productos[identificador]
        else:
            print('El producto con ese identificador no esta registrado')

    def precioBebidas(self,nombre = None):
        total = 0
        if nombre == None :
            for i in self.productos:
                if issubclass(i,bebidas):
                    total = total + i.getPrecio()
        else:
            for i in self.productos:
                if issubclass(i,bebidas) and (i.marca == nombre):
                    total = total + i.getPrecio()
        return total

    def mostrarInfoBebida(self):
        for i in self.productos:
            if issubclass(i,bebidas):
                print(i.__dict__)
