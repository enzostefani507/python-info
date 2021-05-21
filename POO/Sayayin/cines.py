import datetime as dt

class Complejos:
    def __init__(self):
        self.cines = []

    def getCines(self):
        return self.cines

    def agregarCine(self,cine):
        self.cines.append(cine)
        
    cinesPROP = property(getCines,agregarCine)

class Cine:
    def __init__(self):
        self.salas = []
        self.ventas = []

    def getSalas(self):
        return self.salas
    
    def agregarSala(self,sala):
        self.salas.append(sala)

    def registrarVenta(self,venta):
        self.ventas.append(venta)

    salasPROP = property(getSalas,agregarSala)

class Pelicula:
    def __init__(self,nombre,mayores,genero,duracion):
        self.nombre = nombre
        self.mayores = mayores
        self.genero = genero
        self.duracion = duracion

    def getDuracion(self):
        return self.duracion

    def getNombre(self):
        return self.nombre
    
    def cambiarNombre(self,nuevo_nombre):
        self.nombre = nuevo_nombre
    
    def getMayores(self):
        return self.mayores
    
    def cambiarMayor(self,nuevo_mayor):
        self.mayores = nuevo_mayor

    def getGenero(self):
        return self.genero

    def cambiarGenero(self,nuevo_genero):
        self.genero = nuevo_genero

    def informarCalificacion(self):
        if self.mayores:
            print("Pelicula para MAYORES")
        else:
            print("Pelicula apta para todo publico")

    nombrePROP = property(getNombre,cambiarNombre)
    generoPROP = property(getGenero,cambiarGenero)
    mayoresPROP = property(getMayores,cambiarMayor)
    duracionPROP = property(getDuracion)

class Funcion:
    def __init__(self,pelicula,fecha_desde, fecha_hasta,tipo_edad,tipo_funcion,numero):
        self.pelicula = pelicula
        self.fecha_desde = dt.datetime.strptime(fecha_desde,'%d/%m/%Y %H:%M:%S')
        self.fecha_hasta = dt.datetime.strptime(fecha_hasta,'%d/%m/%Y %H:%M:%S')
        self.tipo_edad = tipo_edad
        self.tipo_funcion = tipo_funcion
        self.numero = numero

    def getNumero(self):
        return self.numero

    def getPelicula(self):
        return self.pelicula

    def cambiarPelicula(self,nuevoNombre):
        self.pelicula = nuevoNombre

    def getDesde(self):
        return self.fecha_desde

    def getHasta(self):
        return self.fecha_hasta
    
    def getTipoEdad(self):
        return self.tipo_edad
    
    def getTipoFuncion(self):
        return self.tipo_funcion

    peliculaPROP = property(getPelicula,cambiarPelicula)
    fecha_desdePROP = property(getDesde)
    fecha_hastaPROP = property(getHasta)

class Sala:
    def __init__(self,capacidad):
        self.funciones = []
        self.capacidad = capacidad

    def obtenerFuncion(self,numero_funcion):
        for i in self.funciones:
            if i.getNumero() == numero_funcion:
                return i

    def getCapacidad(self):
        return self.capacidad

    def getFunciones(self):
        return self.funciones

    def agregarFunciones(self,funcion):
        self.funciones.append(funcion)

    def cambiarCapacidad(self,nueva_capacidad):
        self.capacidad = nueva_capacidad
    
    capacidadPROP = property(getCapacidad,cambiarCapacidad)
    funcionesPROP = property(getFunciones,agregarFunciones)

class Entrada:
    def __init__(self,nro_venta, funcion_numero, sala, nombre_pelicula, fecha_hora, precio, tipo, mayores):
        self.nro_venta = nro_venta
        self.fecha_venta = dt.datetime.now()
        self.funcion_numero = funcion_numero
        self.sala = sala
        self.nombre_pelicula = nombre_pelicula
        self.fecha_hora = dt.datetime.strptime(fecha_hora,'%d/%m/%Y %H:%M:%S')
        self.precio = precio
        self.tipo = tipo
        self.mayores = mayores

    def entradaValida(self,funcion_numero):
        funcion = self.sala.obtenerFuncion(funcion_numero)
        if funcion == None:
            return False

        actual = dt.datetime.today()

        if actual > (funcion.getDesde()-dt.timedelta(0,600,0)) and actual < funcion.getHasta():
            return True
        else:
            return False

#Desarrollo
complejo = Complejos()

p1 = Pelicula("Miedo 1",True,"Terror",180)
p2 = Pelicula("Argentina",False,"Comedia",80)

f1 = Funcion(p1,'26/12/2020 17:25:00','26/12/2020 19:30:0',"MAYOR","estreno",1)
f2 = Funcion(p2,'26/12/2020 17:25:00','26/12/2020 19:30:0',"MENOR","normal",2)

s1 = Sala(5)
s2 = Sala(10)

s1.agregarFunciones(f1)
s2.agregarFunciones(f2)

c1 = Cine()

c1.agregarSala(s1)
c1.agregarSala(s2)

e1 = Entrada(1,1,s1,"Miedo",'26/12/2020 17:45:00',300,"MENOR",True)