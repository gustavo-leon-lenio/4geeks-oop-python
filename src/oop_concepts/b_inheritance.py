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


class ClasePadre:  # Parent Class ( Super Class)
    # Define las propiedades de la clase padre aquí
    # Otro nombre que se le puede dar a la clase padre es Clase Base o Super Clase
    pass


class ClaseHija(ClasePadre):  # Child Class (Sub Class)
    # Definir atributos o métodos adicionales aquí
    pass


class Madre:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __repr__(self) -> str:
        return f"{self.nombre}-{self.apellido}"


class Hijo(Madre):
    pass


mamá = Madre("Claudina", "Cortéz")
hija = Hijo("Nataly", "Cortéz")
# hijo = Hijo("Enzo", "Cortéz")
# hijo_2 = Hijo("Manuel", "Cortéz")

print(mamá)
print(hija)
# print(hijo)
# print(hijo_2)
# ir a lamina
