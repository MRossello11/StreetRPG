import enum


class TipoEfecto(enum.Enum):
    QUITAR_VIDA = 0
    AUMENTO_VIDA = 1
    INTERCAMBIO_VIDA = 2
    ATURDIR = 3
    DEFENSA = 4
