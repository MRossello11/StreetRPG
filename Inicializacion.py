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
    listaEfectos.append(Efecto("Daño", TipoEfecto.QUITAR_VIDA, 1.15, 1))     # 0
    listaEfectos.append(Efecto("Cura", TipoEfecto.AUMENTO_VIDA, 1, 1))       # 1
    listaEfectos.append(Efecto("Quemazón", TipoEfecto.QUITAR_VIDA, 0.5, 3))  # 2
    listaEfectos.append(Efecto("Aturdimiento", TipoEfecto.ATURDIR, 0.6, 1))  # 3


def habilidades():
    listaHabilidades.append(Habilidad(0, "Ataque Base", 75, 10, 30, 5, [listaEfectos[0]]))
    listaHabilidades.append(Habilidad(10, "Basculo napalm", 90, 20, 40, 5, [listaEfectos[0], listaEfectos[2]]))
    listaHabilidades.append(Habilidad(20, "Encanto", 25, 10, 60, 10, [listaEfectos[0], listaEfectos[3]]))
    listaHabilidades.append(Habilidad(11, "Daga", 65, 20, 30, 10, [listaEfectos[0]]))
    listaHabilidades.append(Habilidad(21, "Robo", 20, 10, 20, 0, [listaEfectos[0]]))


def personajes():
    listaPersonajes = [Personaje(1, "Mago", 600, [listaHabilidades[0], listaHabilidades[1], listaHabilidades[2]]),
                       Personaje(2, "Ladron", 700, [listaHabilidades[0], listaHabilidades[3], listaHabilidades[4]])]
    return listaPersonajes
