import random

class Objeto:
    def __init__(self, simbolo, nombre):
        self.simbolo = simbolo
        self.nombre = nombre

    def efecto(self, jugador):
        pass

class Roca(Objeto):
    def __init__(self):
        super().__init__('⛰', 'Roca')

class Fruta(Objeto):
    def __init__(self):
        super().__init__('🍍', 'Fruta')

    def efecto(self, jugador):
        jugador.vidas += 1
        print("Te encontraste una piña mi broken vidas+1")

class Serpiente(Objeto):
    def __init__(self):
        super().__init__('🐍', 'Serpiente')

    def efecto(self, jugador):
        jugador.vidas -= 1
        print("TE MORDIO UNA SERPIENTE    VIDAS -1")

class Escorpion(Objeto):
    def __init__(self):
        super().__init__('🦂', 'Escorpión')

    def efecto(self, jugador):
        jugador.vidas -= 1
        print("TE PICO UN ESCORPION   VIDAS -1")

class Cocodrilo(Objeto):
    def __init__(self):
        super().__init__('🐊', 'Cocodrilo')

    def efecto(self, jugador):
        jugador.vidas = 0
        jugador.encontró_cocodrilo = True
        print("TE COMIO EL COCODRILO    FIN")

class Llave(Objeto):
    def __init__(self):
        super().__init__('🗝', 'Llave')

    def efecto(self, jugador):
        jugador.encontró_llave = True
        print("ENCONTRASTE LA LLAVE, PUEDES SALIR!")