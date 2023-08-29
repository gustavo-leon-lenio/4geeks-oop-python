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


# pero que sucede si quisiéramos que hijo tuviera un atributo extra


class Hijo(Madre):
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad


mamá = Madre("Claudina", "Cortéz")
hija = Hijo("Nataly", "Cortéz")
# hijo = Hijo("Enzo", "Cortéz")
# hijo_2 = Hijo("Manuel", "Cortéz")

print(mamá)
print(hija)
# print(hijo)
# print(hijo_2)
# *************** ir a b_inheritance_2.py
