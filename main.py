from Juego import Juego

if __name__ == '__main__':
    while True:
        juego = Juego().partida()
        if input("Jugar otra vez? [S/N] ").lower() == "S":
            continue
        else:
            print("Hasta la próxima!")
            break
