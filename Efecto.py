class Efecto:
    def __init__(self, nombre, tipoEfecto, multiplicador, numTurnos):
        self.nombre = nombre
        self.tipoEfecto = tipoEfecto
        self.multiplicador = multiplicador
        self.dagnoBase = 1
        self.numTurnos = numTurnos
        self.numTurnosRestantes = numTurnos

    def __repr__(self):
        return self.nombre
