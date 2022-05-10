class Jugador:
    def __init__(self, nombre, cpu):
        self.nombre = nombre
        self.cpu = cpu  # True si es una maquina, False para humano
        self.personaje = None

    def __repr__(self):
        return self.nombre
