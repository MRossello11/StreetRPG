class Personaje:
    def __init__(self, *args):
        # constructor a partir de otro Personaje
        if isinstance(args[0], Personaje):
            self.nombre = args[0].nombre
            self.vida = args[0].vida
            self.vidaRestante = args[0].vidaRestante
            self.habilidades = args[0].habilidades

        # constructor a partir de atributos (para evitar objetos duplicados)
        else:
            self.nombre = args[0]  # nombre del personaje
            self.vida = args[1]  # puntos de vida del personaje
            self.vidaRestante = args[1]  # vida restante del presonaje
            self.habilidades = args[2]  # array de habilidades
        self.efectos = []  # efectos en accion
        self.turnosBloqueado = 0  # turnos que tiene que saltar
        self.turnosDefensa = 0  # turnos en los que no recibe dagno

    def __repr__(self):
        return self.nombre + ": " + str(self.vida) + "HP"

    def cambiarVida(self, puntos):
        self.vidaRestante += puntos
