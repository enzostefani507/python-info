productos = list()
entidades = list()

class producto:
    def __init__(self,nombre,cantidad):
        self.nombre = nombre
        self.cantidad = cantidad
        productos.append(self)

    def set_cantidad(self,nueva_cantidad):
        self.cantidad = nueva_cantidad


class perecedero(producto):
    def __init__(self,nombre,cantidad,dias):
        super().__init__(nombre,cantidad)
        self.dias = dias

    def __str__(self):
        return f'{self.nombre}'
    
class noPerecedero(producto):
    def __init__(self,nombre,cantidad,tipo = 'Def'):
        super().__init__(nombre,cantidad)
        self.tipo = tipo
        productos.append(self)

    def __str__(self):
        return f'{self.nombre}'

class entidad:
    def __init__(self,nombre):
        self.nombre = nombre
        entidades.append(self)
    
    def __str__(self):
        return self.nombre

p1 = perecedero('a',4,5)
p2 = noPerecedero('b',5)
p3 = perecedero('c',2,54)

e1 = entidad('primer entidad')
e2 = entidad('segunda entidad')

def calcular(productos,entidades):
    for i in entidades:
        for j in productos:
            print(f'{i}:{j}')
            cantidad = int(j.cantidad)
            cantidad_repartida = cantidad // len(entidades)
            print('     Entrega: {}'.format(cantidad_repartida))
            j.set_cantidad(int(j.cantidad)-cantidad_repartida)
            if hasattr(j,'dias'):
                if int(j.dias)< 10:
                    print('     Entrega hoy')
                elif int(j.dias)< 31:
                    print('     Entrega en la semana')
            else:
                print('     Fecha a elegir')

calcular(productos,entidades)