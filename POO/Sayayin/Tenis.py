class Jugador:
    def __init__(self,nombre):
        self.nombre = nombre
        self.puntuacion = 0
        self.game = 0
        self.set_deuce()
        self.seT = 0
    
    def crear_puntos_tie_brake(self):
        self.__puntos_tie_brake = 0

    def get_puntos_tie_breake(self):
        return self.__puntos_tie_brake

    def inc_unidad_puntuacion_tie_brake(self):
        self.__puntos_tie_brake += 1

    def get_set(self):
        return self.__set

    def set_set(self,numero):
        self.__set = numero

    def get_deuce(self):
        return self.__deuce

    def agregar_deuce(self,nuevo_valor):
        self.__deuce.append(nuevo_valor)

    def set_deuce(self):
        self.__deuce = []

    def get_game(self):
        return self.__game

    def set_game(self,nuevo_game):
        self.__game = nuevo_game

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self,nuevo_nombre):
        self.__nombre = nuevo_nombre

    def get_puntuacion(self):
        return self.__puntuacion

    def set_puntuacion(self,nueva_puntuacion):
        self.__puntuacion = nueva_puntuacion

    def inc_puntuacion(self):
        actual = self.get_puntuacion
        if actual == 0:
            self.puntuacion = 15
        elif actual == 15:
            self.puntuacion = 30
        elif actual == 30:
            self.puntuacion += 10
        else:
            self.puntuacion += 10
    
    nombre = property(get_nombre,set_nombre)
    game = property(get_game,set_game)
    puntuacion = property(get_puntuacion,set_puntuacion)
    deuce = property(get_deuce,agregar_deuce)
    seT = property(get_set,set_set)

class Marcador:
    def __init__(self,j1,j2):
        self.jugador1 = j1
        self.jugador2 = j2
        self.es_tie = False
    
    def get_tie(self):
        return self.__es_tie
    
    def set_tie(self,valor):
        self.__es_tie = valor

    def get_jugador1(self):
        return self.__jugador1

    def set_jugador1(self,nuevo_jugador1):
        self.__jugador1 = nuevo_jugador1

    def get_jugador2(self):
        return self.__jugador2

    def set_jugador2(self,nuevo_jugador2):
        self.__jugador2 = nuevo_jugador2

    def __evaluar_deuce(self,jug1,jug2):
        if jug1 == True:
            self.jugador1.deuce = 1
            self.jugador2.deuce = 0
        else:
            self.jugador1.deuce = 0
            self.jugador2.deuce = 1

    def __incrementar_puntuaciones(self,jug1,jug2):
        if jug1 == True:
                self.jugador1.inc_puntuacion()
        else:
            self.jugador2.inc_puntuacion()

    def __game(self,jug1,jug2):
        if (self.jugador1.puntuacion > 40 and self.jugador2.puntuacion < 40):
                    self.jugador1.game = (self.jugador1.game)+1
        elif (self.jugador1.puntuacion < 40 and self.jugador2.puntuacion > 40): 
            self.jugador2.game = (self.jugador2.game)+1
        elif (self.jugador1.puntuacion >= 40 and self.jugador2.puntuacion >= 40) and abs(self.jugador1.puntuacion -self.jugador2.puntuacion) >= 20:
            if self.jugador1.puntuacion > self.jugador2.puntuacion:
                print (f'Gana {self.jugador1}')
                self.jugador1.game = (self.jugador1.game)+1
            else:
                print (f'Gana {self.jugador2}')
                self.jugador2.game = (self.jugador2.game)+1
        elif (self.jugador1.puntuacion >= 40 and self.jugador2.puntuacion >= 40) and abs(self.jugador1.puntuacion -self.jugador2.puntuacion) < 20:
            self.__evaluar_deuce(jug1,jug2)
            if len(self.jugador1.deude) == 2 and len(self.jugador2.deude) == 2:
                if self.jugador1.deude[-1] == 1 and self.jugador1.deude[-2]==1:
                    print (f'Gana {self.jugador1}')
                    self.jugador1.game = (self.jugador1.game)+1
                elif self.jugador2.deude[-1] == 1 and self.jugador2.deude[-2]==1:
                    print (f'Gana {self.jugador2}')
                    self.jugador2.game = (self.jugador2.game)+1

    def __incrementar_set(self):
        if self.jugador1.game == 6 and abs(self.jugador1.game-self.jugador2.game)>=2:
            self.jugador1.seT = (self.jugador1.seT)+1
            self.__set_cero
        elif self.jugador2.game == 6 and abs(self.jugador1.game-self.jugador2.game)>=2:
            self.jugador2.seT == (self.jugador2.seT)+1
            self.__set_cero
            
    def __set_cero(self):
        self.jugador1.game = 0
        self.jugador2.game = 0
        self.jugador1.puntuacion = 0
        self.jugador2.puntuacion = 0

    def __run_tie_brake(self,jug1,jug2):
        if jug1 == True:
            self.jugador1.inc_unidad_puntuacion_tie_brake()
        else:
            self.jugador2.inc_unidad_puntuacion_tie_brake()                    

        self.__evaluar_fin_time_breake
        self.__run_tie_brake_largo
    
    def __evaluar_fin_time_breake(self,jug1,jug2):
        if self.jugador1.get_puntos_tie_breake() == 7 and abs(self.jugador1.get_puntos_tie_breake()-self.jugador2.get_puntos_tie_breake())>=2:
            return self.jugador1
        elif self.jugador2.get_puntos_tie_breake() == 7 and abs(self.jugador1.get_puntos_tie_breake()-self.jugador2.get_puntos_tie_breake())>=2:
            return self.jugador2

    def run_tie_brake_largo(self,jug1,jug2)
        if self.jugador1.get_puntos_tie_breake() >= 6 and abs(self.jugador1.get_puntos_tie_breake()-self.jugador2.get_puntos_tie_breake())<=2:
            return self.jugador2
        elif self.jugador2.get_puntos_tie_breake() >= 6 and abs(self.jugador1.get_puntos_tie_breake()-self.jugador2.get_puntos_tie_breake())<=2:
            return self.jugador2

    def jugar(self,jug1=None,jug2=None):
        if jug1 == jug2:
            print("Valores incorrectos")
        else:
            if not(self.es_tie):
                self.__incrementar_puntuaciones(jug1,jug2)
                self.__incrementar_puntuaciones(jug1,jug2)
                self.__incrementar_set()
                if self.jugador1.game == 6 and self.jugador2.game == 6:
                    self.jugador1.crear_puntos_tie_brake()
                    self.jugador2.crear_puntos_tie_brake()
                    self.set_tie(True)
            else:
                self.__run_tie_brake(jug1,jug2)
                    
    jugador1 = property(get_jugador1,set_jugador1)
    jugador2 = property(get_jugador2,set_jugador2)
    es_tie = property(get_tie,set_tie)

