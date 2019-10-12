from __future__ import annotations

from src import Papel, Tijera
from src.Resultado import Resultado
from src.Mano import Mano


class Piedra(Mano):

    def jugar(self, otraMano: Mano) -> Resultado:
        return otraMano.jugarContraPiedra(self)

    def jugarContraPapel(self, papel: Papel) -> Resultado:
        return Resultado.PERDER

    def jugarContraTijera(self, tijera: Tijera) -> Resultado:
        return Resultado.GANAR

    def jugarContraPiedra(self, piedra: Piedra) -> Resultado:
        return Resultado.EMPATAR