class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    # Getter para obtener el nombre
    def get_nombre(self):
        return self.__nombre

    # Setter para actualizar el nombre con validación
    def set_nombre(self, nuevo_nombre):
        if len(nuevo_nombre) > 0:
            self.__nombre = nuevo_nombre

    # Getter para obtener la edad
    def get_edad(self):
        return self.__edad

    # Setter para actualizar la edad con validación
    def set_edad(self, nueva_edad):
        if nueva_edad >= 0:
            self.__edad = nueva_edad
