from __future__ import annotations
import abc

from src import Resultado, Papel, Tijera, Piedra


class Mano(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def jugar(self, otraMano: Mano) -> Resultado:
        pass

    @abc.abstractmethod
    def jugarContraPapel(self, papel: Papel) -> Resultado:
        pass

    @abc.abstractmethod
    def jugarContraTijera(self, tijera: Tijera) -> Resultado:
        pass

    @abc.abstractmethod
    def jugarContraPiedra(self, piedra: Piedra) -> Resultado:
        pass