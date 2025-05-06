class Jugador:
    def __init__(self):
        self.vidas = 5
        self.encontró_llave = False
        self.encontró_cocodrilo = False

    def estado(self):
        print(f"Vidas: {'❤' * self.vidas} ({self.vidas})")
