from Juego import Juego

if __name__ == '__main__':
    print("Bienvenido a StreetRPG")
    print("")
    while True:
        juego = Juego().partida()
        if input("Jugar otra vez? [S/N] ").lower() == "s":
            continue
        else:
            print("Hasta la próxima!")
            break
