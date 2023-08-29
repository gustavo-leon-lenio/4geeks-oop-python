import random


class Dado:
    def __init__(self, lados):
        self.lados = lados

    def lanzar(self):
        return random.randint(1, self.lados)


d4 = Dado(4)
d5 = Dado(6)
