class Libro:
    def __init__(self, titulo, autor, año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
        self.esta_prestado = False

    def prestar(self):
        if not self.esta_prestado:
            self.esta_prestado = True
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' ya está prestado.")

    def retornar(self):
        if self.esta_prestado:
            self.esta_prestado = False
            print(f"El libro '{self.titulo}' ha sido devuelto.")
        else:
            print(f"El libro '{self.titulo}' no estaba prestado.")

    def detalles(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de Publicación: {self.año_publicacion}")
        estado = "Prestado" if self.esta_prestado else "Disponible"
        print(f"Estado: {estado}")


# Crear instancias de libros
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)
libro2 = Libro("El principito", "Antoine de Saint-Exupéry", 1943)

# Usar los métodos de las instancias
libro1.detalles()
libro1.prestar()
libro1.detalles()
libro1.retornar()
libro1.detalles()

libro2.detalles()
libro2.prestar()
