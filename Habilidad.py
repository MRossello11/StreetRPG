import random


class Habilidad:
    def __init__(self, codigoHabilidad, nombre, dagno, probFallo, probCritico, probBackFire, efectos):
        self.codigoHabilidad = codigoHabilidad  # codigo identificador de la habilidad
        self.nombre = nombre  # nombre de la habilidad
        self.dagno = dagno  # cantidad de dagno base
        self.probFallo = probFallo  # probabilidad de que la habilidad falle
        self.probCritico = probCritico  # probabilidad de que la habilidad haga dagno critico
        self.probBackFire = probBackFire  # probabilidad de que la habilidad haga backfire
        self.efectos = efectos  # lista de efectos que provoca la habilidad
        self.modificarDagnoBaseEfectos()

    def __repr__(self):
        return self.nombre + " " + str(self.dagno)

    def modificarDagnoBaseEfectos(self):
        for efecto in self.efectos:
            efecto.dagnoBase = self.dagno

    def evaluarProbabilidades(self):
        listaProbabilidades = []  # donde True = se aplica la probabilidad, False = no se aplica

        # prob fallo
        probabilidad = random.randint(0, 100)
        if probabilidad <= self.probFallo:
            # si falla, no hay mas probabilidades que evaluar
            return listaProbabilidades

        # prob critico
        probabilidad = random.randint(0, 100)
        if probabilidad <= self.probCritico:
            listaProbabilidades.append(True)
        else:
            listaProbabilidades.append(False)

        # prob backfire
        probabilidad = random.randint(0, 100)
        if probabilidad <= self.probBackFire:
            listaProbabilidades.append(True)
        else:
            listaProbabilidades.append(False)

        return listaProbabilidades
