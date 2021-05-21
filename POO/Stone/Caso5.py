class Tiempo:
    def valido(self,kwargs):
        if kwargs["hora"] < 0 or kwargs["hora"] >24:
            return False
        elif kwargs["minuto"]< 0 or kwargs["minuto"] >60:
            return False
        elif kwargs["segundo"]< 0 or kwargs["segundo"] >60: 
            return False
        return True

    def __init__(self,**kwargs):
        if self.valido(kwargs):
            self.__hora =  None
            self.__minuto = None
            self.__segundo = None
            if len(kwargs) == 3:
                self.__hora =  kwargs["hora"]
                self.__minuto = kwargs["minuto"]
                self.__segundo = kwargs["segundo"]
            elif len(kwargs) == 2:
                self.__hora =  kwargs["hora"]
                self.__minuto = kwargs["minuto"]
                self.__segundo = 00
            elif len(kwargs) == 1:
                self.__hora =  kwargs["hora"]
                self.__minuto = 00
                self.__segundo = 00
        else:
            raise Exception("Datos erroneos")

    def getHora(self):
        """Comentario en 3 comillas sirve para que despues sea visible desde help de la clase"""
        return self.__hora

    def getMinuto(self):
        return self.__minuto


    def getSegundo(self):
        return self.__segundo

    def __str__(self):
        try:
            if self.__hora !=None and self.__minuto !=None and self.__segundo !=None:
                return f'{self.__hora}:{self.__minuto}:{self.__segundo}'
        except Exception as e: 
            return "Ha ocurrido un error =>"+ type(e).__name__

    def setHora(self,hora):
        self.__hora = hora

    def setMinuto(self,Minuto):
        self.__minuto = Minuto

    def setSegundo(self,segundo):
        self.__segundo = segundo

    def mostrar(self,separador):
        return f'{self.__hora}{separador}{self.__minuto}{separador}{self.__segundo}'

t1 = Tiempo(hora=22,minuto=30,segundo=33)
print(t1.mostrar(":"))

