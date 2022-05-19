import copy
import random

import Inicializacion
from Jugador import Jugador
from Personaje import Personaje
from TipoEfecto import TipoEfecto
from TipoMensaje import TipoMensaje


class Juego:
    CRITICO = 1.5

    def __init__(self):
        Inicializacion.inicio()
        self.jugador1 = None
        self.jugador2 = None
        self.personajes = Inicializacion.personajes()
        self.jugadores = []

    # decision de la cantidad de jugadores
    def eleccionJugadores(self):

        numJugadores = 2 if input("Numero de jugadores (1 o 2): ") == "2" else 1
        print("Modo seleccionado: ", numJugadores, " jugador(es)")
        self.jugador1 = Jugador(input("Introduzca su nombre (Jugador 1): "), False)
        self.jugador2 = Jugador("CPU", True)
        # si ambos jugadores son humanos, se sobreescribe el jugador2
        if numJugadores == 2:
            self.jugador2 = Jugador(input("Introduzca su nombre (Jugador 2): "), False)

        self.jugadores = [self.jugador1, self.jugador2]

    def eleccionPersonajes(self):
        try:
            for i in self.jugadores:
                # muestra de los personajes
                contador = 0
                for personaje in self.personajes:
                    print("(", contador, ")", personaje)
                    contador += 1

                # eleccion de los personajes
                # si el jugador actual no es la maquina
                if i.cpu is False:
                    i.personaje = Personaje(self.personajes[copy.deepcopy(int(input(f"Turno {i.nombre}: ")))])

                # si el jugador actual es la maquina (se elige el personaje aleatoriamente)
                else:
                    i.personaje = Personaje(self.personajes[copy.deepcopy(random.randint(0, len(self.personajes) - 1))])

                print(i.nombre, " ha elegido ", i.personaje)

        except ValueError:
            print("Alguien ha seleccionado un numero de jugador invalido")
            self.eleccionPersonajes()

    def mostrarStatusPartida(self, jugador):
        turno = 0
        turno2 = 1
        if jugador == 1:
            turno = 1
            turno2 = 0

        print(f"                                     {self.jugadores[turno2].nombre}")
        print("                                     ============================")
        print(f"                                     {self.jugadores[turno2].personaje.nombre}  HP: "
              f"{self.jugadores[turno2].personaje.vidaRestante} / "
              f"{self.jugadores[turno2].personaje.vida}     ")
        contador = 1
        for i in self.jugadores[turno2].personaje.habilidades:
            print("                                    ", contador, ". ", i)
            contador += 1
        print("                                     ============================")

        print(self.jugadores[turno].nombre)
        print("============================")
        print(
            f"{self.jugadores[turno].personaje.nombre}  HP: "
            f"{self.jugadores[turno].personaje.vidaRestante} / {self.jugadores[turno].personaje.vida}    ")
        contador = 1
        for i in self.jugadores[turno].personaje.habilidades:
            print(contador, ". ", i)
            contador += 1
        print("============================")
        print("                                     ")

    def partida(self):
        # preparativos
        self.eleccionJugadores()
        self.eleccionPersonajes()

        # se elige la persona que empieza primero
        turnoJugador = 0
        turnoContrario = 1

        while True:
            # turno jugador
            for jugador in self.jugadores:
                # si el jugador esta bloquedado (por estar aturdido, por ejemplo)
                if jugador.personaje.turnosBloqueado > 0:
                    print(jugador.nombre, "esta aturdido!")
                    # se le resta un turno de bloqueo y se pasa al siguiente
                    jugador.personaje.turnosBloqueado -= 1
                    # se vuelven a invertir los turnos
                    if turnoJugador == 0:
                        turnoJugador = 1
                        turnoContrario = 0
                    else:
                        turnoJugador = 0
                        turnoContrario = 1
                    continue
                print("Turno ", jugador.nombre)
                habilidad = None

                # muestra de status de partida y eleccion de habilidad
                self.mostrarStatusPartida(turnoJugador)
                if jugador.cpu is False:
                    habilidad = self.eleccionHabilidad(jugador)
                else:
                    # la cpu elige una habilidad aleatoria
                    habilidad = jugador.personaje.habilidades[random.randint(0, len(jugador.personaje.habilidades) - 1)]

                print(jugador.nombre, " va a usar ", habilidad)
                # se evaluan las probabilidades de la habilidad escogida
                probabilidades = None
                probabilidades = habilidad.evaluarProbabilidades()

                if len(probabilidades) == 0:
                    self.mensajeAtaque(TipoMensaje.FALLO, jugador, 0)

                # si no falla
                else:
                    efecto = copy.deepcopy(habilidad.efectos[0])

                    # se agnaden los efectos de la habilidad usada para que luego se apliquen
                    # si el ataque es critico, se aplican los efectos extra que puedan haber
                    if probabilidades[0] is True:
                        # si es critico y solo hay un efecto, este hace mas dagnoBase
                        if len(habilidad.efectos) == 1:
                            efecto.dagnoBase *= self.CRITICO  # se aplica el critico
                            self.appendEfectos(efecto, turnoJugador, turnoContrario)
                        # todo: revisar la aplicacion de los efectos extra
                        # si se tienen que aplicar efectos extra
                        else:
                            # se aplican tantos efectos extra como haya
                            for efecto in habilidad.efectos:
                                self.appendEfectos(efecto, turnoJugador, turnoContrario)

                    # si el ataque no es critico (ataque normal), solo se aplica el primer efecto
                    else:
                        self.appendEfectos(efecto, turnoJugador, turnoContrario)

                    # en caso de backfire se hace lo contrario que el ataque normal
                    if probabilidades[1] is True:
                        self.appendEfectos(efecto, turnoContrario, turnoJugador)

                # agnadidos los efectos, se aplican
                self.aplicarEfectos()

                input("Presione ENTER para terminar turno")

                # comprobacion de la vida de ambos jugadores (si alguno no tiene vida el otro gana si tiene vida)
                if self.comprobarVida():
                    return

                # se invierten los turnos
                if turnoJugador == 0:
                    turnoJugador = 1
                    turnoContrario = 0
                else:
                    turnoJugador = 0
                    turnoContrario = 1

    def eleccionHabilidad(self, jugador):
        while True:
            contador = 1
            print("Habilidades:")
            for i in jugador.personaje.habilidades:
                print("(", contador, ") ", i)
                contador += 1

            try:
                # la habilidad introducida tiene que ser un numero valido y ser una habilidad reconocida
                return jugador.personaje.habilidades[int(input("Accion: ")) - 1]
            except ValueError:
                print("Opcion no contemplada")
                continue
            except IndexError:
                print("Opcion no contemplada")
                continue

    def mensajeAtaque(self, mensaje, jugador, dagno=0, turnos=0, efecto=""):

        # mensaje normal
        if mensaje == TipoMensaje.NORMAL:
            print(jugador.nombre, " ha recibido", dagno, " de dagno!")
        # mensaje critico
        elif mensaje == TipoMensaje.CRITICO:
            print(jugador.nombre, " ha hecho un critico!")

        # mensaje fallo
        elif mensaje == TipoMensaje.FALLO:
            print(jugador.nombre, " ha fallado!")

        # mensaje backfire
        elif mensaje == TipoMensaje.BACKFIRE:
            print(jugador.nombre, " se ha herido a si mismo! (", dagno, "puntos de dagno)")

        # mensaje efecto (dagno hecho por un efecto duradero)
        elif mensaje == TipoMensaje.EFECTO:
            print(jugador.nombre, " ha recibido ", dagno, " puntos de dagno por ", efecto,
                  " (", turnos, " turnos restantes)")

        # mensaje defensa
        elif mensaje == TipoMensaje.DEFENSA:
            print("Ataque bloqueado!")

        # mensaje curacion
        elif mensaje == TipoMensaje.CURACION:
            print(jugador.nombre, "se ha curado", dagno, "puntos")

        # mensaje aturdimiento
        elif mensaje == TipoMensaje.ATURDIMENTO:
            print(jugador.nombre, " aturdido por", turnos, " turnos!")

    # aplica efectos y manda los mensajes apropiados
    def aplicarEfectos(self):
        for jugador in self.jugadores:
            # si no hay efectos a aplicar, se salta al siguiente jugador
            if len(jugador.personaje.efectos) > 0:
                # se aplica efecto a efecto de mas antiguo a mas nuevo
                for efecto in jugador.personaje.efectos:
                    if efecto.numTurnosRestantes <= 0:
                        jugador.personaje.efectos.remove(efecto)
                        continue

                    # efectos que quitan vida
                    if efecto.tipoEfecto == TipoEfecto.QUITAR_VIDA:

                        dagno = efecto.dagnoBase
                        jugador.personaje.cambiarVida(-dagno)

                        if efecto.nombre != "Daño":
                            self.mensajeAtaque(TipoMensaje.EFECTO, jugador, dagno,
                                               efecto.numTurnosRestantes, efecto)
                        else:
                            self.mensajeAtaque(TipoMensaje.NORMAL, jugador, dagno)

                    elif efecto.tipoEfecto == TipoEfecto.ATURDIR:
                        jugador.personaje.turnosBloqueado += 1
                        self.mensajeAtaque(TipoMensaje.ATURDIMENTO, jugador, jugador)

                    elif efecto.tipoEfecto == TipoEfecto.AUMENTO_VIDA:
                        aumento = efecto.dagnoBase
                        jugador.personaje.cambiarVida(aumento)
                        self.mensajeAtaque(TipoMensaje.CURACION, jugador, aumento)

                    # elif efecto.tipoEfecto == TipoEfecto.DEFENSA:

                    efecto.numTurnosRestantes -= 1

                for efecto in jugador.personaje.efectos:
                    # se quitan los efectos que no tengan mas turnos
                    if efecto.numTurnosRestantes == 0:
                        jugador.personaje.efectos.remove(efecto)
                        # print(efecto, " eliminado")
                        efecto.numTurnosRestantes = efecto.numTurnos

    def comprobarVida(self):
        # empate (ambos jugadores no tienen vida)
        if self.jugador2.personaje.vidaRestante <= 0 and self.jugador1.personaje.vidaRestante <= 0:
            print("Empate!")
            return True
        # evaluacion si alguien ha ganado
        # gana jugador2 (jugador1 tiene 0 o menos de vida y el jugador2, mas de 0 de vida)
        elif self.jugador1.personaje.vidaRestante <= 0 and self.jugador2.personaje.vidaRestante > 0:
            print(self.jugador2.nombre, "ha ganado!")
            return True

        # gana jugador1 (jugador2 tiene 0 o menos de vida y el jugador1, mas de 0 de vida)
        elif self.jugador2.personaje.vidaRestante <= 0 and self.jugador1.personaje.vidaRestante > 0:
            print(self.jugador1.nombre, "ha ganado!")
            return True

        else:
            return False

    def appendEfectos(self, efecto, turnoJugador, turnoContrario):
        # si el efecto extra es de aumento de vida, va para el jugador
        if efecto.tipoEfecto == TipoEfecto.AUMENTO_VIDA \
                or efecto.tipoEfecto == TipoEfecto.DEFENSA:
            self.jugadores[turnoJugador].personaje.efectos.append(copy.deepcopy(efecto))

        # intercambio de vida
        elif efecto.tipoEfecto == TipoEfecto.INTERCAMBIO_VIDA:
            self.jugadores[turnoJugador].personaje.cambiarVida(+efecto.dagnoBase)
            # self.mensajeAtaque(TipoMensaje.CURACION, self.jugadores[turnoJugador], efecto.dagnoBase)
            self.jugadores[turnoContrario].personaje.cambiarVida(-efecto.dagnoBase)
            # self.mensajeAtaque(TipoMensaje.NORMAL, self.jugadores[turnoContrario], efecto.dagnoBase)

        # tipo efecto normal
        else:
            self.jugadores[turnoContrario].personaje.efectos.append(copy.deepcopy(efecto))
            self.mensajeAtaque(TipoMensaje.CRITICO, self.jugadores[turnoJugador])
