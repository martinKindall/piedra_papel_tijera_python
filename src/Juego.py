from src.Papel import Papel
from src.Resultado import Resultado
from src.Piedra import Piedra
from src.Tijera import Tijera

manoJugador1 = Piedra()
manoJugador2 = Piedra()

resultadoJugador2: Resultado = manoJugador1.jugar(manoJugador2)

if resultadoJugador2 == Resultado.GANAR:
    print("El jugador 2 ganó")
elif resultadoJugador2 == Resultado.EMPATAR:
    print("Empate")
elif resultadoJugador2 == Resultado.PERDER:
    print("El jugador 1 ganó")
else:
    raise("Resultado desconocido")