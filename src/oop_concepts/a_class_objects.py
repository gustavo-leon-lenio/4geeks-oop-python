"""Ejemplo de Clase y Objeto.

Todas las definiciones de clase comienzan con la palabra clase en inglés "class",
seguida del nombre de la clase y dos puntos.

El nombre de la clase debe seguir el estilo de Pascal Case
que escribe en mayúscula la letra inicial de cada palabra compuesta.

Si se trata de una palabra Auto
Si se trata de multiples palabras MiAuto

El cuerpo de una clase es cualquier código que está sangrado
o indentado debajo de su definición
"""


class Auto:
    def __init__(self, color, motor, modelo):
        self.color = color
        self.motor = motor
        self.modelo = modelo

    def acelerar(self):
        pass

    def imprimir_auto(self):
        print(self.color, self.motor, self.modelo)


# "🔴" "🟢" "🟡"


auto_rojo = Auto("🔴", "gasolina", "sedan")
auto_rojo_2 = Auto("🔴", "gasolina", "sedan")
auto_verde = Auto("🟢", "eléctrico", "SUV")
auto_amarillo = Auto("🟡", "diesel", "pick up")

auto_rojo.imprimir_auto()
auto_amarillo.imprimir_auto()
auto_verde.imprimir_auto()


print(auto_rojo_2 == auto_rojo)

### Ir a Lamina
