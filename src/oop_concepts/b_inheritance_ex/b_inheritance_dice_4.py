import random  # noqa: D100


class Dado:
    """Clase de un dado Genérico."""

    def __init__(self, lados):
        """Implementa constructor para establecer cómo atributo la cantidad de lados deseados."""
        self.lados = lados

    def lanzar(self):
        """Hereda de clase Dado, Implementamos un Dado de 4 Lados."""
        return random.randint(1, self.lados)


class D4(Dado):
    """Hereda de clase Dado, Implementamos un Dado específicamente de 4 Lados."""

    def __init__(self):
        """Llama al constructor padre para establecer atributo de 4 lados."""
        super().__init__(4)


class D6(Dado):
    """Hereda de clase Dado, Implementamos un Dado específicamente de 6 Lados."""

    def __init__(self):
        """Llama al constructor padre para establecer atributo de 6 lados."""
        super().__init__(6)


class D8(Dado):
    """Hereda de clase Dado, Implementamos un Dado específicamente de 8 Lados."""

    def __init__(self):
        """Llama al constructor padre para establecer atributo de 8 lados."""
        super().__init__(8)


class D10(Dado):
    """Hereda de clase Dado, Implementamos un Dado específicamente de 10 Lados."""

    def __init__(self):
        """Llama al constructor padre para establecer atributo de 10 lados."""
        super().__init__(10)


class D12(Dado):
    """Hereda de clase Dado, Implementamos un Dado específicamente de 12 Lados."""

    def __init__(self):
        """Llama al constructor padre para establecer atributo de 12 lados."""
        super().__init__(12)


class D20(Dado):
    """Hereda de clase Dado, Implementamos un Dado específicamente de 20 Lados."""

    def __init__(self):
        """Llama al constructor padre para establecer atributo de 20 lados."""
        super().__init__(20)


class D6Cargado(Dado):
    """Hereda de clase Dado, Implementamos un Cargado que solo Lanza 6."""

    def __init__(self):
        """Llama al constructor padre para establecer atributo de 6 lados."""
        super().__init__(6)

    def lanzar(self):
        """Sobrescribe el método lanzar original de la clase padre.

        para establecer que siempre retorne 6
        """
        return 6


"""Creamos instancias de las Clases (objetos)."""
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
