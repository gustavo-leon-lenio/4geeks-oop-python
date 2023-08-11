class Carta:
    def __init__(self, palo, valor):
        self.palo = palo
        self.valor = valor

    def __repr__(self) -> str:
        """
        Las f-strings, también conocidas como literales de cadena formateados,
        son una característica de formateo de cadenas introducida en Python 3.6.
        Son una forma más sencilla y legible de formatear cadenas en comparación
        con métodos anteriores como el uso de % o la función str.format().

        En una f-string, puedes incluir expresiones Python dentro
        de las llaves {} dentro de una cadena.
        Estas expresiones se evaluarán y se insertarán en la cadena resultante.
        Las f-strings se reconocen por la letra 'f' (o 'F')
        que se coloca antes de la cadena de formato.
        """
        return f"{self.valor}-{self.palo}"


class Baraja:
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
        comodines = ["🤡"] * 2

        # Aquí recorremos por cada palo y cada valor para ir creando cada carta
        for palo in palos:
            for valor in valores:
                self.cards.append(Carta(palo, valor))

        for comodin in comodines:
            self.cards.append(Carta("X", comodin))


if __name__ == "__main__":
    tres_de_corazones = Carta("♥️", 3)
    print(tres_de_corazones)
    baraja_francesa = Baraja()
    print(baraja_francesa.cards)
