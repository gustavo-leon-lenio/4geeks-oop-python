class Carta:
    def __init__(self, palo, valor):
        self.palo = palo
        self.valor = valor

    def __repr__(self) -> str:
        return f"{self.valor}-{self.palo}"


class Baraja:
    def __init__(self) -> None:
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
        self.cards = []
        for palo in palos:
            for valor in valores:
                self.cards.append(Carta(palo, valor))


if __name__ == "__main__":
    tres_de_corazones = Carta("♥️", 3)
    print(tres_de_corazones)
    baraja_francesa = Baraja()
    print(baraja_francesa.cards)
