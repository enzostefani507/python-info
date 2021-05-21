from datetime import datetime, date, time, timedelta

class Pedido:
    def __init__(self,nombreCliente,pizza,cantidad,hora,minuto,demora_estimada):
        self._nombre_cliente = nombreCliente
        self.pizza = pizza
        self.cantidad = cantidad
        self.fecha = datetime.now()
        self.hora_entrega = time(hora,minuto,0)
        self.demora_estimada = demora_estimada
        self.estado = "Pendiente"

    def cambiarEstado(self):
        self.estado = "Listo"
        print("Factura generada")

    def getFecha(self):
        return self.fecha

    def getPizza(self):
        return self.pizza
    
    def getCantidad(self):
        return self.cantidad

class Menu:
    """Menu dispondra de listado de pizzas y las dispondra de forma oportuna"""
    def __init__(self,pizzas):
        self._pizzas = pizzas
    
    def getPizzas(self):
        return self._pizzas

    def mostrarMenu(self):
        print('MENU CLIENTE')
        for pi,i in enumerate(self.getPizzas(),0):
            print(f'{pi}]Nombre:{i.nombre}')
            print(f'\t Precio:{i.precio}')
            print(f'\t Tamaño:{i.tamano}')
            print(f'\t Tipo:{i.tipo}')
            print(f'\t Ingredientes:')
            for num,elem in enumerate(i.ingredientes,1):
                print('\t\t'+str(num)+")",str(elem))

class Pizza:
    """
    Almacena todos los atributos de la pizza, tales como:
        nombre
        ingredientes
        precio
        tamano
        tipo
    Todos estan disponibles por sus set o get, ademas de por property
    """
    def __init__(self,nombre,precio,ingredientes,tamano,tipo):
        self._nombre = nombre
        self._ingredientes = ingredientes
        self._precio = precio
        try:
            if tamano in [8,10,12] and tipo in ["piedra","parrilla","molde"]:
                self._tamano = tamano
                self._tipo = tipo
        except ValueError:
            print("Los tamaños pueden ser 8,10 o 12\n Los tipos pueden ser piedra,parrilla o mole")
    
    def getTamano(self):
        return self._tamano

    def getTipo(self):
        return self._tipo

    def setTamano(self,tamano):
        self._tamano = tamano
        return self.getTamano()

    def setTipo(self,tipo):
        self._tipo = tipo
        return self.getTipo()

    def getPrecio(self):
        return self._precio

    def setPrecio(self,precio):
        self._precio = precio
        return self.getPrecio()

    def getNombre(self):
        return self._nombre
    
    def setNombre(self,nombre):
        self._nombre = nombre
        return self.getNombre()

    def getIngredientes(self):
        return self._ingredientes    

    def agregarIngredientes(self,*ingredientes):
        for i in ingredientes:
            self._ingredientes.append(i)
        return self.getIngredientes()

    def getId(self):
        return self.getNombre()+str(self.getTamano())+self.getTipo()

    nombre = property(getNombre,setNombre)
    precio = property(getPrecio,setPrecio)
    ingredientes = property(getIngredientes,agregarIngredientes)
    tamano = property(getTamano,setTamano)
    tipo = property(getTipo,setTipo)

class Pizzeria:
    def __init__(self):
        #self.pizzas = [] A modo de ejemplo cargo una pizza por defecto
        self.pizzas = [Pizza("Muzzarella",500,['4 quesos','Salsa tomate','Aceitunas'],8,"piedra")]
        self.pedidos = []
    
    def instanciarMenu(self):
        self.menu = Menu(self.pizzas)

    def agregarPizza(self):
        """Se encarga de solicitar los datos al usuario e isntancair la clase pizza con los mismos, retornando el objeto"""
        nombre = input("Ingrese nombre de la pizza: ")
        precio = int(input("Ingrese precio de la pizza: " ))
        todos_ingredientes = input("Ingrese todos los ingiredientes separados por espacio: ")
        ingredientes = todos_ingredientes.split()
        tamano = int(input("Ingrese el tamaño: \n8\n10\n12\n>>"))
        tipo = input("Ingrese un tipo: \npiedra\nparrilla\nmole\n>>")
        pizza = Pizza(nombre,precio,ingredientes,tamano,tipo)
        self.pizzas.append(pizza)
    
    def registrarPedido(self):
        nombre_cliente = input("Ingrese el nombre del cliente: ")
        self.menu.mostrarMenu()
        i = int(input("Seleccione el numero correspondiente a su pizza: "))
        pizza = self.menu.getPizzas()[i]
        cantidad = int(input("Ingrese la cantidad de solicita de esta pizza: "))
        hora = int(input("Ingrese hora de entrega: "))
        minuto = int(input("Ingrese minuto de entrega: "))
        demora_estimada = input("Ingrse la demora estimada: ")
        p = Pedido(nombre_cliente,pizza,cantidad,hora,minuto,demora_estimada)
        self.pedidos.append(p)

    def ingresosFech(self,fechaInicio,fechaFin):
        """Ingresos (recaudaciones) por períodos de tiempo. """
        formato_fecha = "%d/%m/%Y"
        fecha_inicial = datetime.strptime(fechaInicio, formato_fecha)
        fecha_final  = datetime.strptime(fechaFin, formato_fecha)
        tot = 0
        for i in self.pedidos:
            if (i.getFecha() < fecha_final) and (i.getFecha() > fecha_inicial):
                tot = tot + (i.getPizza().getPrecio())*i.getCantidad()
        return tot
            
    def pedidosFech(self,fechaInicio,fechaFin):
        """Pedidos (cantidad y monto) por períodos de tiempo. """
        formato_fecha = "%d/%m/%Y"
        fecha_inicial = datetime.strptime(fechaInicio, formato_fecha)
        fecha_final  = datetime.strptime(fechaFin, formato_fecha)
        res = []
        tot = [0,0]
        for i in self.pedidos:
            if (i.getFecha() < fecha_final) and (i.getFecha() > fecha_inicial):
                res.append([i.getCantidad(),(i.getPizza().getPrecio())*i.getCantidad()])
                tot[1] = tot[1] + (i.getPizza().getPrecio())*i.getCantidad()
                tot[0] = tot[0] + i.getCantidad()
        return res,tot
        
    def variedadTiposMasPedidos(self):
        estadistica = dict()         
        for i in self.pedidos:
            if i.getPizza().getId() in self.pedidos:
                estadistica[i.getPizza().getId()] += i.getCantidad()
            else:
                estadistica[i.getPizza().getId()] = i.getCantidad()
        return estadistica

#Desarrollo
pi = Pizzeria()
pi.instanciarMenu()
pi.registrarPedido()
print(pi.ingresosFech("01/05/2020","01/05/2021"))
print(pi.pedidosFech("01/05/2020","01/05/2021"))
print(pi.variedadTiposMasPedidos())