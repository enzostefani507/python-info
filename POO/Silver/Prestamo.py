from datetime import datetime, date, time, timedelta

#Controlar porque muestra los prestamos en clientes y clientes en prpestamos

prestamos = []
clientes = []
tope = 500

def verificarPrestamo(Prestamo,prestamos,tope):
    total = 0
    for i in prestamos:
        total = total + i.valor
    return (total + Prestamo.valor) < tope

class Cliente:
    def __init__(self,dni,nombre,apellido1,apellido2,telefono,celular):
        self.dni = dni
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.telefono = telefono
        self.celular = celular

    def __main__(self):
        return "Cliente"

    def __str__(self):
        return (str(self.dni)+" "+self.nombre+" "+str(self.celular))

class Prestamo:
    def validoCuotas(self,fechasPago):
        return len(fechasPago) <= 6

    def validoNumero(self,numero):
        return numero > 0

    def validoPrestamo(self,valor):
        return (valor > 0)

    def __init__(self,numero,solicitante,valor,fechasPago,fecha_auto,fecha_entrega,fechaTope='01/01/2022'):
        
        self.tope = tope
        self.fechaTope = datetime.strptime(fechaTope,'%d/%m/%Y')

        if fecha_entrega == None:
            fe = datetime.strptime(fecha_auto, '%d/%m/%Y')+timedelta(days=7)
        else:
            fe = datetime.strptime(fecha_entrega, '%d/%m/%Y')
        
        cuotas = []
        k = 0
        for i in fechasPago:
            conv = datetime.strptime(i, '%d/%m/%Y')
            cuotas.append(conv)
            if k == 0:
                k += 1
                if conv < fe + timedelta(days=30):
                    raise Exception ("La fecha de primer cuota debe ser superior a 30 dias respecto de la entrega")
        
        fa = datetime.strptime(fecha_auto, '%d/%m/%Y')
        if fa.day > 20 or fa > self.fechaTope:
            raise Exception("Se encuentra fuera de plazo")
        
        if self.validoCuotas(cuotas) and self.validoNumero(numero) and self.validoPrestamo(valor) and solicitante.__main__()=="Cliente":
            self.fechas = cuotas
            self.valor = valor
            self.numero = numero

        else:
            raise Exception ("Alguno de los parametros es errroneo")
        self.fecha_autorizacion = fa
        self.fecha_entrega = fe
        if verificarPrestamo(self,prestamos,tope) == False:
            raise Exception("El tope fue excedido")

    def impimir(self):
        return self.__dict__

c1 = Cliente(123424,"Enzo","Benites","Lopez",45645,3452)
c2 = Cliente(41234,"Elon","Musk","nose",234,4234)
clientes.append(c1)
clientes.append(c2)
p1 = Prestamo(1,c1,250,['15/03/2021'],'15/12/2020','15/01/2021')
prestamos.append(p1)

def buscar_clientes(clientes,dni):
    res = []
    for i in clientes:
        if i.dni == dni:
            return res.append(i)
    

def cargar_cliente():
    dni = int(input("Ingrese un dni: "))
    nombre = input("Ingrese un nombre: ")
    apellido1 = input("Ingrese un apellido: ")
    apellido2 = input("Ingrse segundo apellido: ")
    telefono = int(input("Ingrese un telefono fijo: "))
    celular = int (input("Ingrese un celular: "))
    c = Cliente(dni,nombre,apellido1,apellido2,telefono,celular)
    return c

def cargar_prestamos():
    
    numero = int(input("Ingrese numero de prestamo: "))
    dni = int(input("Ingrese dni del solicitante: "))
    solicitante = buscar_clientes(clientes,dni)
    valor = int(input("Ingrese un valor de prestamo: "))
    fechasPago = input("Ingrese fecha de pagos")
    fecha_auto = input("Ingrese fecha de autorizacion")
    fecha_entrega = input("Ingrese fecha de entrega")

    p = Prestamo(numero,solicitante,valor,fechasPago,fecha_auto,fecha_entrega,fechaTope='01/01/2022')
    
    return p

def modificartope(tope,nuevo):
    tope = nuevo

def main(clientes,prestamos,tope):
    while True:
        print("1.Cargar cliente")
        print("2.Cargar prestamo")
        print("3.Ver clientes")
        print("4.Ver prestamos")
        print("5.Salir")
        o = int(input("Seleccione\n>>"))
        print("---------------")
        if o == 1:
            clientes.append(cargar_cliente())
            print("Cliente registrado")
            print("---------------")
        elif o ==2:
            prestamos.append(cargar_prestamos())
            print("Prestamo cargado")
            print("---------------")
        elif o == 3:
            print("--Clientes--")
            for i in clientes:
                print(i.__dict__)
            print("---------------")
        elif o == 4:
            print("--Prestamos--")
            for j in prestamos:
                print(j.__dict__)
            print("---------------")
        elif o==5:
            print("Fin")
            break 
        else:
            print("Opcion no valida")
            
    
main(clientes,prestamos,tope)
