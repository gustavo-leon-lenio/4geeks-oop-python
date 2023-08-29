""" Etiqueta Especial super()

"""


class Padre:
    def __init__(self, nombre):
        self.nombre = nombre


class Hijo(Padre):
    def __init__(self, nombre, edad):
        super().__init__(nombre)
        self.edad = edad


# class Padre:
#     def __init__(self, nombre):
#         self.nombre = nombre

#     def saludar(self):
#         print(f"Hola, soy {self.nombre}.")


# class Hijo(Padre):
#     def __init__(self, nombre, edad):
#         super().__init__(nombre)
#         self.edad = edad

#     def saludar(self):
#         super().saludar()
#         print(f"Tengo {self.edad} años.")


### ir a lamina
