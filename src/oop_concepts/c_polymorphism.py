
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def emitir_sonido(self):
        return "Algún sonido genérico"

class Perro(Animal):
    # "Canis familiaris" 🐶
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

    def emitir_sonido(self):
        return "¡Guau!"

class Gato(Animal):
    # "Felis catus" 🐱
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

    def emitir_sonido(self):
        return "Miau!"


animal_generico = Animal("Animal Generico")
gato = Gato("Michi", "Chantilly")
perro = Perro("Firulai", "Corgi")
print(animal_generico.emitir_sonido())
print(gato.emitir_sonido())
print(perro.emitir_sonido())

##############################################################################

class Pokemon:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def speak(self):
        pass

    def attack(self):
        pass

class Pikachu(Pokemon):
    def attack(self):
        return f"{self.name} used Thunderbolt!"

class Charmander(Pokemon):
    def attack(self):
        return f"{self.name} used Ember!"

class Squirtle(Pokemon):
    def attack(self):
        return f"{self.name} used Water Gun!"

# Polymorphism in action
pokemon_team = [
    Pikachu("Pikachu", 25),
    Charmander("Charmander", 20),
    Squirtle("Squirtle", 22)
]

for pokemon in pokemon_team:
    print(pokemon.speak())
    print(pokemon.attack())
    print("=" * 20)















class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def obtener_salario(self):
        return self.salario


class EmpleadoFullTime(Empleado):
    def __init__(self, nombre, salario, beneficios):
        super().__init__(nombre, salario)
        self.beneficios = beneficios

    def obtener_salario(self):
        return self.salario + self.beneficios


class EmpleadoPartTime(Empleado):
    def __init__(self, nombre, salario, horas_trabajo):
        super().__init__(nombre, salario)
        self.horas_trabajo = horas_trabajo

    def obtener_salario(self):
        salario_tiempo_completo = 40
        salario_medio_tiempo = (
            self.salario / salario_tiempo_completo
        ) * self.horas_trabajo
        return salario_medio_tiempo




class Pokemon:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def speak(self):
        return f"{self.name}, I choose you!"

    def attack(self):
        pass


class Pikachu(Pokemon):
    def attack(self):
        return f"{self.name} used Thunderbolt!"


class Charmander(Pokemon):
    def attack(self):
        return f"{self.name} used Ember!"


class Squirtle(Pokemon):
    def attack(self):
        return f"{self.name} used Water Gun!"


# Polymorphism in action
pokemon_team = [
    Pikachu("Pikachu", 25),
    Charmander("Charmander", 20),
    Squirtle("Squirtle", 22),
]

for pokemon in pokemon_team:
    print(pokemon.speak())
    print(pokemon.attack())
    print("=" * 20)
