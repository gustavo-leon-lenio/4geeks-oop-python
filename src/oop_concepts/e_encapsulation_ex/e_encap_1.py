class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


persona_1 = Persona("Alice", 38)
persona_2 = Persona("Mario", 23)


print(persona_1.nombre)
print(persona_2.nombre)
persona_1.nombre = "Amanda"
print(persona_1.nombre)
