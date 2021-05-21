    class Empleado:
    def __init__(self, nombre, apellido,sueldo):
        self.nombre = nombre
        self.apellido = apellido
        self.sueldo = sueldo

    def nombre_completo(self):
        return "{} {}".format(self.nombre, self.apellido)

    def aumentar_sueldo(self, monto):
        self.sueldo = self.sueldo + monto