from random import shuffle


class CartaLuno:
    def __init__(self, color, valor):
        self.color = color
        self.valor = valor

    def __repr__(self) -> str:
        return f"{self.valor}-{self.color}"


class BarajaLuno:
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
        specials = ["+4", "W", "+4", "W", "+4", "W", "+4", "W"]
        self.__cartas = []
        for color in colores:
            for valor in valores:
                self.__cartas.append(CartaLuno(color, valor))

        for special in specials:
            self.__cartas.append(CartaLuno("*", special))

    def revolver(self):
        shuffle(self.__cartas)

    def sacar_carta(self):
        return self.__cartas.pop()


baraja_uno = BarajaLuno()
# print("Antes de Revolver", baraja_uno.cartas)
print("*" * 80)
baraja_uno.revolver()
# print("Después de Revolver", baraja_uno.cartas)

carta = baraja_uno.sacar_carta()
print(carta)
