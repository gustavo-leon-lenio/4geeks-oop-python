import random


class CartaUno:
    def __init__(self, color, valor):
        self.color = color
        self.valor = valor

    def __repr__(self) -> str:
        return f"{self.valor}-{self.color}"


class BarajaUno:
    def __init__(self) -> None:
        colores = ["🟡", "🔵", "🔴", "🟢"]
        valores = [
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "0",
            "+2",
            "reversa",
            "salto",
        ]
        specials = ["+4", "W"] * 4
        self.cartas = []
        for color in colores:
            for valor in valores:
                self.cartas.append(CartaUno(color, valor))

        self.cartas.extend(specials)

    def revolver(self):
        random.shuffle(self.cartas)


if __name__ == "__main__":
    baraja_uno = BarajaUno()
    baraja_uno.revolver()
    print(baraja_uno.cartas)
    baraja_uno.revolver()
    print(baraja_uno.cartas)
