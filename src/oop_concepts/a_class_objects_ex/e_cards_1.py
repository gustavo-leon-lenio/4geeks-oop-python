class Carta:
    def __init__(self, palo, valor):
        """
        Constructor de la clase Carta.
        Representa una carta de una baraja de cartas estándar.

        :param palo: El palo de la carta (corazones, diamantes, tréboles, espadas)
        ["♠️", "♥️", "♦️", "♣️"]
        :type palo: str
        :param valor: El valor numérico o simbólico de la carta (2, 3, ..., 10, J, Q, K, A).
        :type valor: str
        """
        self.palo = palo
        self.valor = valor

    def __repr__(self) -> str:
        """
        Devuelve una representación legible de la instancia de Carta.
        :return: Una cadena que muestra el estado actual de la instancia.
        :rtype: str
        """
        return f"{self.valor}-{self.palo}"


tres_de_corazones = Carta("♥️", 3)
dos_de_diamante = Carta("♦️", 2)
print(tres_de_corazones)
print(dos_de_diamante)

dos_de_trebol = Carta("♣️", 2)
print(dos_de_trebol)


# ir a 2
