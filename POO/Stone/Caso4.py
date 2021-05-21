class Contacto:
    def __init__(self,nombre,telefono,email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email


    def __str__(self):
        return self.nombre + "-" +str(self.telefono) +"-" +self.email


    def setNombre(self,nombre):
        self.nombre = nombre


    def setTelefono(self,telefono):
        self.telefono = telefono
    

    def setEmail(self,email):
        self.email = email



class Agenda:
    def __init__(self,nombre):
        self.contactos = list()
        self.nombre = nombre
    
    
    def añadirContacto(self,contact):
        self.contactos.append(contact)
        return self


    def buscarContacto(self,dato):
        for i in self.contactos:
            if dato in (i.nombre,i.telefono,i.email):
                return i
    

    def editarContacto(self,dato,**kwargs):
        c = self.buscarContacto(dato)
        for key,value in kwargs.items():
            if key == "nombre":
                c.setNombre(value)
            if key == "telefono":
                c.setTelefono(value)
            if key == "email":
                c.setEmail(value)
        return c


    def __str__(self):
        print(f'##{self.nombre}')
        for i in self.contactos:
            print(i.__dict__)

    def listar(self):
        return self.contactos


#Para no tener que cargar todo a mano - ejemplo
a1 = Agenda("A1")
c1 = Contacto("Enzo",324233,"asdfa@gmail.com")
c2 = Contacto("Ricardo",323123,"xyza@gmail.com")
a1.añadirContacto(c1)
a1.añadirContacto(c2)
a1.editarContacto("Enzo",telefono=14322,email="asssas@hotmail.com")
agendas = []
agendas.append(a1)
print(a1.buscarContacto('Enzo'))
#=================================================


def menu_principal():
    print(f'=======Menu=======')
    print(f'1. Ver agendas')
    print(f'2. Crear Agenda')
    print(f'3. Salir')
    o = int(input(">> "))
    return o


def crearAgenda():
    print(f'===Nueva Agenda===')
    nombre = input('Ingrese un nombre')
    nueva = Agenda(nombre)
    agendas.append(nueva)
    print("Se registro la agenda")
    print('1. Volver menu principal')
    print('2. Registrar contacto')
    o = input('>> ')
    return o,nueva


def registrar_contacto(agenda):
    print('==Nuevo Contacto==')
    nombre = input('Ingrese el nombre: \n>>')
    telefono = input('Ingrese el telefono: \n>>')
    email = input('Ingrese el email: \n>>')
    nuevo_contacto = Contacto(nombre,telefono,email)
    agenda.añadirContacto(nuevo_contacto)
    print('Se añadio el contacto')


def listar_agendas(registros):
    for i in range(0,len(registros)):
        print(str(i)+"-"+registros[i].nombre)


def menu_agendas(registros):
    print('===Menu Agendas===')
    listar_agendas(registros)
    e = int(input('Seleccione una: \n>>'))
    print('1. Ver contactos')
    print('2. Editar Contacto')
    print('3. Añadir Contacto')
    print('4. Buscar Contacto')
    i = int(input('>> '))
    if i == 1:
        todos = registros[e].listar()
        for i in todos:
            print(i)
    elif i == 2:
        dato = input('Ingrese nombre del contacto: ')
        telefono = int(input('Ingrese el nuevo telefono'))
        email = int(input('Ingrese el nuevo email'))
        registros[e].editarContacto(dato,telefono,email)
    elif i == 3:
        registrar_contacto(e)
    elif i == 4:
        dato = input('Ingrese datos del contacto: ')
        print(registros[e].buscarContacto(dato))
    else:
        print("Opcion no valida")


def main(registros):
    while True:
        e = menu_principal()
        if e == 1:
            menu_agendas(registros)
        elif e == 2:
            r = crearAgenda()
            """r sera una tupla, el primer elemento la respuesta y el segundo la agenda creada"""
            if r[0] == 1:
                #Volver al menu
                pass
            elif r[0] == 2:
                registrar_contacto(r[1])
            else:
                print("Opcion no valida")
        elif e == 3:
            break
        else:
            print("Opcion no valida")

main(agendas)