class ClasePadre:
    # Define las propiedades de la clase padre aquí
    # Otro nombre que se le puede dar a la clase padre es Clase Base o Super Clase
    pass


class ClaseHija(ClasePadre):
    # Definir atributos o métodos adicionales aquí
    pass


class Padre:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Hijo(Padre):
    pass


mamá_1 = Padre("Claudina", "Cortéz")
hija = Hijo("Nataly", "Cortéz")

print(mamá_1.nombre, mamá_1.apellido)
print(hija.nombre, hija.apellido)

