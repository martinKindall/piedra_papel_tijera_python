from __future__ import annotations

from src import Tijera, Piedra
from src.Resultado import Resultado
from src.Mano import Mano


class Papel(Mano):

    def jugar(self, otraMano: Mano) -> Resultado:
        return otraMano.jugarContraPapel(self)

    def jugarContraPapel(self, papel: Papel) -> Resultado:
        return Resultado.EMPATAR

    def jugarContraTijera(self, tijera: Tijera) -> Resultado:
        return Resultado.PERDER

    def jugarContraPiedra(self, piedra: Piedra) -> Resultado:
        return Resultado.GANAR