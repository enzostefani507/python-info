class persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

class cuenta:
    def __init__(self,persona,cantidad):
        self.titular = persona
        if cantidad < 0:
            pass
        else:
            self.cantidad = cantidad
    
    def ingrearCantidad(self,cantidad):
        if cantidad < 0:
            pass
        else:
            self.cantidad += cantidad
        return self.cantidad

    def mostrar(self):
        print(self.__dict__)
    
    def retirar(self,retira):
        self.cantidad -= retira
        return self.cantidad

    def getCantidad(self):
        return self.cantidad

class cuenta_joven(cuenta):
    def esTitularValido(self,edad):
        return (edad >= 18) and (edad <= 25)

    def __init__(self,persona,cantidad,bonificacion):
        super().__init__(persona,cantidad)
        self.bonificacion = bonificacion
        if (self.esTitularValido(persona.edad) == False):
            raise Exception("Su edad no es vaida")

    def mostrar(self):
        return f'Cuenta joven\n Bonificacion: {self.bonificacion}'
    
p1 = persona("Enzo",18)
c1 = cuenta_joven(p1,500,150)

print(c1.mostrar())

c1.retirar(40)

print(c1.getCantidad())

