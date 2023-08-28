class Pokemon:
    def __init__(self, nombre, nivel):
        self.nombre = nombre
        self.nivel = nivel

    def hablar(self):
        pass

    def atacar(self):
        pass


class Pikachu(Pokemon):
    def __init__(self, nivel):
        super().__init__("Pikachu", nivel)

    def atacar(self):
        return f"¡{self.nombre} usó Impactrueno!"


class Charmander(Pokemon):
    def __init__(self, nivel):
        super().__init__("Charmander", nivel)

    def atacar(self):
        return f"¡{self.nombre} usó Ambar!"


class Squirtle(Pokemon):
    def __init__(self, nivel):
        super().__init__("Squirtle", nivel)

    def atacar(self):
        return f"¡{self.nombre} usó Pistola de Agua!"


# "Un Lenguaje Común para Objetos Diferentes"

# "El Mismo Verbo, Distintos Sustantivos"

pokemon_team = [
    Pikachu(25),
    Charmander(20),
    Squirtle(22),
]

for pokemon in pokemon_team:
    print(pokemon.hablar())
    print(pokemon.atacar())
    print("=" * 20)
