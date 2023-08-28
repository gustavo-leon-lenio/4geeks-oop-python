class Carta:
    def __init__(self, palo, valor):
        """
        Constructor de la clase Carta.
        Representa una carta de una baraja de cartas estándar.

        :param palo: El palo de la carta (corazones, diamantes, tréboles, espadas)
        :type palo: str
        :param valor: El valor numérico o simbólico de la carta (2, 3, ..., 10, J, Q, K, A).
        :type valor: str
        """
        self.palo = palo
        self.valor = valor

    def __repr__(self) -> str:
        """
        Devuelve una representación legible de la instancia de MiClase.

        :return: Una cadena que muestra el estado actual de la instancia.
        :rtype: str
        """
        return f"{self.valor}-{self.palo}"


class BarajaFrancesa:
    def __init__(self) -> None:
        self.cards = []
        palos = ["♠️", "♥️", "♦️", "♣️"]
        valores = [
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "J",
            "Q",
            "K",
            "A",
        ]
        comodines = ["🤡", "🤡"]

        # Aquí recorremos por cada palo y cada valor para ir creando cada carta
        for palo in palos:
            for valor in valores:
                self.cards.append(Carta(palo, valor))

        for comodin in comodines:
            self.cards.append(Carta("X", comodin))


baraja_francesa = BarajaFrancesa()
print(baraja_francesa.cards)

# ir a 3
