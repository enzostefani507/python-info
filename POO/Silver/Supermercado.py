class Producto:
    def __init__(self,nombre,precio,cuidado=False):
        self.nombre = nombre
        self.precio = precio
        self.cuidado = cuidado

class PrimeraNecesidad(Producto):
    def __init__(self,nombre,precio,cuidado,descuento):
        super().__init__(nombre,precio,cuidado)
        self.descuento = descuento

    def obtener_descuento(self):
        return self.precio*self.descuento

class Supermercado():
    def __init__(self,nombre,direccion):
        self.nombre = nombre
        self.productos = []
        self.direccion = direccion
    
    def agregar(self,producto):
        self.productos.append(producto)

    def total_productos(self):
        return self.productos
    
    def total_precio(self):
        tot = 0
        for i in self.productos:
            tot = tot + i.precio
        return tot

s1 = Supermercado("Chino","San Lorenzo")
p1 = PrimeraNecesidad("Mila",300,True,0.9)
p2 = PrimeraNecesidad("Mayo",50,True,0.9)
p3 = Producto("Pan",30,False)
s1.agregar(p1)
s1.agregar(p2)
s1.agregar(p3)

print(p1.obtener_descuento())
