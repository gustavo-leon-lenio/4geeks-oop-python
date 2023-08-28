class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def emitir_sonido(self):
        return "Algún sonido genérico"


class Perro(Animal):
    # "Canis familiaris" 🐶
    def emitir_sonido(self):
        return "¡Guau!"


class Gato(Animal):
    # "Felis catus" 🐱
    def emitir_sonido(self):
        return "Miau!"


animal_generico = Animal("Animal Generico")
gato = Gato("Michi", "Chantilly")
perro = Perro("Firulai", "Corgi")
print(animal_generico.emitir_sonido())  # "Algún sonido genérico"
print(gato.emitir_sonido())  # "Miau!"
print(perro.emitir_sonido())  # "¡Guau!"
