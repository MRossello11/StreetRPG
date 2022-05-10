import enum


class TipoMensaje(enum.Enum):
    NORMAL = 0
    CRITICO = 1
    FALLO = 2
    BACKFIRE = 3
    EFECTO = 4
