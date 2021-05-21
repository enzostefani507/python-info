import datetime as dt

class Alquiler:
    def __init__(self,cuit):
        self.__dia = dt.datetime.today()
        self.descuento = 0
        self.cuit = cuit
        self.descuentoMiercoles()
        self.setCUIT(cuit)

    def setCUIT(self,nuevo_cuit):
        self.__cuit = nuevo_cuit

    def getCUIT(self,nuevo_cuit):
        return self.__cuit

    def setDescuento(self,nuevo_descuento):
        self.__descuento = nuevo_descuento

    def getDia(self):
        return self.__dia

    def descuentoMiercoles(self):
        #El 3 corresponde a los miercoles
        if self.dia == 3:
            self.descuento += 50    

    def getDescuento(self):
        if hasattr(Alquiler,'_Alquiler__descuento'):
            return self.__descuento

    dia = property(getDia)
    descuento = property(getDescuento,setDescuento)
    cuit = property(getCUIT,setCUIT)


class AlquilerHora(Alquiler):
    """El alquiler por hora es de 100"""
    def __init__(self,cuit):
        super().__init__(cuit)
        self.__costo = 100
    
    def getCosto(self):
        return self.__costo

    def cerrarAlquiler(self,horas):
        if hasattr(AlquilerHora,'_AlquilerHora__descuento'):
            if self.cuit.startswith('26'):
                return ((self.costo*horas)-self.descuento)*0.95
            else:
                return (self.costo*horas)-self.descuento
        else:
            return (self.costo*horas)

    costo = property(getCosto)

class AlquilerDia(Alquiler):
    """El cliente paga un monto fijo por día (el día son 24 horas) no importa si el auto se devuelve antes."""
    def __init__(self,dias,cuit):
        super().__init__(cuit)
        self.__dias = dias
        self.__costo = 2000

    def getDias(self):
        return self.__dias

    def getCosto(self):
        return self.__costo

    def cerrarAlquiler(self):
        actual = dt.datetime.today()
        if hasattr(AlquilerDia,'_AlquilerDia__descuento'):
            if self.cuit.startswith('26'):
                c = ((self.costo)-self.descuento)*0.95
            else:
                c = (self.costo)-self.descuento
        else:
            c = (self.costo)
        
        if actual < (actual+dt.timedelta(days=self.dias)):
            return c
        else:
            return c*2

    dias = property(getDias)
    costo = property(getCosto)

class AlquilerKilometraje(Alquiler):
    """El cliente paga un precio fijo por cada kilómetros recorrido durante el período de alquiler. Este tipo de alquiler implica devolución dentro del mismo día de alquiler."""
    def __init__(self,cuit):
        super().__init__(cuit)
        self._costoBase = 100
        self._costoKilometro = 10

    def getCostoBase(self):
        return self._costoBase

    def getCostoKilometro(self):
        return self._costoKilometro

    def cerrarAlquiler(self,recorrido):
        if hasattr(AlquilerDia,'_AlquilerDia_descuento'):
            if self.cuit.startswith('26'):
                return ((self.costoBase)-(self.descuento)+(self.getCostoKilometro*recorrido))*0.95
            else:
                return (self.costoBase)-(self.descuento)+(self.getCostoKilometro*recorrido)
        else:
            return (self.costoBase)+(self.getCostoKilometro*recorrido)

    costoBase = property(getCostoBase)
    costoKilometro = property(getCostoKilometro)
