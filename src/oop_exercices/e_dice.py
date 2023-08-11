import random


class Dado:
    def __init__(self, lados):
        self.lados = lados

    def lanzar(self):
        # roll the dice
        return random.randint(1, self.lados)


class D4(Dado):
    def __init__(self):
        super().__init__(4)


class D6(Dado):
    def __init__(self):
        super().__init__(6)


class D8(Dado):
    def __init__(self):
        super().__init__(8)


class D10(Dado):
    def __init__(self):
        super().__init__(10)


class D12(Dado):
    def __init__(self):
        super().__init__(12)


class D20(Dado):
    def __init__(self):
        super().__init__(20)


class D6Cargado(Dado):
    def __init__(self):
        super().__init__(6)

    def lanzar(self):
        return 6


if __name__ == "__main__":
    # Instanciamos los dados
    d4 = D4()
    d4_2 = D4()
    d6 = D6()
    d8 = D8()
    d10 = D10()
    d12 = D12()
    d20 = D20()
    d6_c = D6Cargado()

    print("Lanzando un dado D4:", d4.lanzar())
    print("Lanzando un dado D4_2:", d4_2.lanzar())
    print("Lanzando un dado D6:", d6.lanzar())
    print("Lanzando un dado D8:", d8.lanzar())
    print("Lanzando un dado D10:", d10.lanzar())
    print("Lanzando un dado D12:", d12.lanzar())
    print("Lanzando un dado D6 Cargado:", d6_c.lanzar())
