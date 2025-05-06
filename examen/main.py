from isla import Isla
from jugador import Jugador

def jugar():
    isla = Isla()
    jugador = Jugador()

    while jugador.vidas > 0 and not jugador.encontró_llave and not jugador.encontró_cocodrilo:
        isla.mostrar_mapa()
        jugador.estado()

        try:
            x = int(input("Escribe la fila (0-5): "))
            y = int(input("Escribe la columna (0-5): "))
        except ValueError:
            print("Numero invalido SOLO USA NUMEROS DEL 0 AL 5")
            continue

        isla.explorar(x, y, jugador)

    print("Fin del juego")
    if jugador.encontró_llave:
        print("Escapaste de la isla GANASTE")
    elif jugador.encontró_cocodrilo:
        print("El cocodrilo te encontró MMSTE")
    else:
        print("Te quedaste sin vidas PERDISTE")

    print("Vidas restantes: {jugador.vidas}")
    print("Mapa completo")
    isla.mostrar_mapa_completo()

    if input("QUIERES VOLVER A JUEGAR??? (s/n): ").lower() == 's':
        jugar()

if __name__ == "__main__":
    jugar()
