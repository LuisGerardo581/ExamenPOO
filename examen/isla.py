import random
from objetos import Roca, Fruta, Serpiente, Escorpion, Cocodrilo, Llave

class Isla:
    def __init__(self):
        self.tamaño = 6
        self.mapa = [[None for _ in range(self.tamaño)] for _ in range(self.tamaño)]
        self.explorado = [[False for _ in range(self.tamaño)] for _ in range(self.tamaño)]
        self.distribuir_objetos()

    def distribuir_objetos(self):
        objetos = [Llave(), Cocodrilo()] + [Fruta() for _ in range(3)] + [Roca() for _ in range(3)] + [Serpiente() for _ in range(2)] + [Escorpion() for _ in range(2)]
        while len(objetos) < self.tamaño * self.tamaño:
            objetos.append(random.choice([Fruta(), Roca(), Serpiente(), Escorpion()]))
        random.shuffle(objetos)
        for i in range(self.tamaño):
            for j in range(self.tamaño):
                self.mapa[i][j] = objetos.pop()

    def mostrar_mapa(self):
        for i in range(self.tamaño):
            for j in range(self.tamaño):
                if self.explorado[i][j]:
                    print(self.mapa[i][j].simbolo, end=' ')
                else:
                    print('❓', end=' ')
            print()

    def mostrar_mapa_completo(self):
        for fila in self.mapa:
            print(' '.join(obj.simbolo for obj in fila))

    def explorar(self, x, y, jugador):
        if not (0 <= x < self.tamaño and 0 <= y < self.tamaño):
            print("Coordenadas inválidas.")
            return False
        if self.explorado[x][y]:
            print("Ya exploraste esta celda.")
            return False
        self.explorado[x][y] = True
        objeto = self.mapa[x][y]
        print(f"Encontraste un(a) {objeto.nombre} {objeto.simbolo}")
        objeto.efecto(jugador)
        return True