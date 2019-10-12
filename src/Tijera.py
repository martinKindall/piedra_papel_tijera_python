from __future__ import annotations

from src import Papel, Piedra
from src.Resultado import Resultado
from src.Mano import Mano


class Tijera(Mano):

    def jugar(self, otraMano: Mano) -> Resultado:
        return otraMano.jugarContraTijera(self)

    def jugarContraPapel(self, papel: Papel) -> Resultado:
        return Resultado.GANAR

    def jugarContraTijera(self, tijera: Tijera) -> Resultado:
        return Resultado.EMPATAR

    def jugarContraPiedra(self, piedra: Piedra) -> Resultado:
        return Resultado.PERDER