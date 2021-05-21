class Libro:
    def __init__(self,titulo,autor,numeroPaginas,calificacion):
        self.titulo = titulo
        self.autor = autor
        self.numeroPaginas = numeroPaginas
        if (calificacion >= 0) and (calificacion <= 10):
            self.calificacion = calificacion
        
    def getTitulo(self):
        return self.titulo
    
    def getAutor(self):
        return self.autor

    def getPaginas(self):
        return self.numeroPaginas
    
    def getCalif(self):
        return self.calificacion

    def setTitulo(self,titulo):
        self.titulo = titulo
    
    def setAutor(self,autor):
        self.autor = autor

    def setPaginas(self,paginas):
        self.numeroPaginas = paginas
    
    def setCalif(self,calificacion):
        self.calificacion = calificacion

class ConjuntoLibros:
    def __init__(self,espacio):
        self.libros = []
        self.espacio = espacio
    
    def añadirLibros(self,libro):
        if libro not in self.libros and len(self.libros)<self.espacio:
            self.libros.append(libro)
        elif len(self.libros)>=self.espacio:
            print("No hay mas espacio")
    
    def eliminarLibro(self,titulo,autor = None):
        if titulo == None and autor == None:
            print("Ingrese los parametros adecuados")
        else:
            for i in self.libros:
                if i.getTitulo == titulo or i.getAutor == autor:
                    self.libros.remove(i)
    
    def mayorCalificacion(self):
        calificaciones = []
        for i in self.libros:
            calificaciones.append(i.getCalif)
        return max(calificaciones)

    def menorCalificacion(self):
        calificaciones = []
        for i in self.libros:
            calificaciones.append(i.getCalif)
        return min(calificaciones)

    def mostrarContenido(self):
        for i in self.libros:
            print(i.__dict__)

c = ConjuntoLibros(3)
l1 = Libro("AM","Gauus",300,5)
l2 = Libro("AM2","Elon",300,5)
l3 = Libro("F","Faraday",300,5)
l4 = Libro("F3","Enzo",300,5)
c.añadirLibros(l1)
c.añadirLibros(l2)
c.añadirLibros(l3)
c.añadirLibros(l4)