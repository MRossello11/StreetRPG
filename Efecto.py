class Efecto:
    def __init__(self, nombre, tipoEfecto, numTurnos):
        self.nombre = nombre
        self.tipoEfecto = tipoEfecto
        self.dagnoBase = 1
        self.numTurnos = numTurnos
        self.numTurnosRestantes = numTurnos

    def __repr__(self):
        return self.nombre
