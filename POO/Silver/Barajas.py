import random

class carta:
    def __init__(self,numero,palo):
        if numero not in (8,9):
            self.numero = numero
        else:
            raise Exception("Numero no valido")
        if palo in("espadas","bastos","oros","copas"):
            self.palo = palo
        else:
            raise Exception("Ese palo no existe")
    
class baraja:
    def __init__(self,cartas):
        self.cartas = []
        self.cartas.extend(list(cartas))
        self.pos = 0
        self.salio = []
    
    def agregar(self,cartas):
        self.cartas.append(cartas)
        return self.cartas

    def barajar(self,cartas):
        random.shuffle(self.cartas)
        return self.cartas

    def siguiente_carta(self):
        elem = self.cartas.pop()
        self.salio.append(elem)
        return elem

    def cartas_disponibles(self):
        return len(self.cartas)

    def dar_cartas(self,numero):
        elementos = []
        for i in range(numero):
            k = self.cartas.pop()
            elementos.append(k)
            self.salio.append(k)
        return elementos
     
    def cartas_monton(self):
        if len(self.salio)==0:
            return 'No salio ninguna carta'
        else:
            return self.salio

    def mostrar_baraja(self):
        return self.cartas
