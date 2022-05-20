import copy

from TipoEfecto import TipoEfecto
from Efecto import Efecto
from Habilidad import Habilidad
from Personaje import Personaje

listaEfectos = []
listaHabilidades = []


def inicio():
    efectos()
    habilidades()
    personajes()


def efectos():
    listaEfectos.append(Efecto("Daño", TipoEfecto.QUITAR_VIDA, 1))  # 0
    listaEfectos.append(Efecto("Cura", TipoEfecto.AUMENTO_VIDA, 1))  # 1
    listaEfectos.append(Efecto("Quemazón", TipoEfecto.QUITAR_VIDA, 3))  # 2
    listaEfectos.append(Efecto("Aturdimiento", TipoEfecto.ATURDIR, 1))  # 3
    listaEfectos.append(Efecto("Intercambio vida", TipoEfecto.INTERCAMBIO_VIDA, 1))  # 4


def habilidades():
    listaHabilidades.append(Habilidad("Ataque Base", 75, 10, 30, 5, [copy.deepcopy(listaEfectos[0])]))  # 0

    listaHabilidades.append(Habilidad("Basculo napalm", 90, 20, 40, 5, [copy.deepcopy(listaEfectos[0]),
                                                                        copy.deepcopy(listaEfectos[2])]))  # 1

    listaHabilidades.append(Habilidad("Encanto", 25, 10, 60, 10, [copy.deepcopy(listaEfectos[0]),
                                                                  copy.deepcopy(listaEfectos[3])]))  # 2

    listaHabilidades.append(Habilidad("Daga", 65, 20, 30, 10, [copy.deepcopy(listaEfectos[0])]))  # 3

    listaHabilidades.append(Habilidad("Robo", 30, 10, 20, 0, [copy.deepcopy(listaEfectos[4])]))  # 4

    listaHabilidades.append(Habilidad("Patada", 115, 50, 30, 45, [copy.deepcopy(listaEfectos[0]),
                                                                  copy.deepcopy(listaEfectos[3])]))  # 5

    listaHabilidades.append(Habilidad("Empujon", 80, 35, 15, 10, [copy.deepcopy(listaEfectos[0])]))  # 6

    listaHabilidades.append(Habilidad("Cura", 50, 20, 5, 1, [copy.deepcopy(listaEfectos[1])]))  # 7


def personajes():
    listaPersonajes = [
        Personaje("Mago", 400, [listaHabilidades[0], listaHabilidades[1], listaHabilidades[2], listaHabilidades[7]]),
        Personaje("Ladron", 700, [listaHabilidades[0], listaHabilidades[3], listaHabilidades[4]]),
        Personaje("Bruto", 900, [listaHabilidades[0], listaHabilidades[4], listaHabilidades[5], listaHabilidades[6]])
        # Personaje("Escudero", 1200, [listaHabilidades[0], listaHabilidades[6]])
    ]
    return listaPersonajes
