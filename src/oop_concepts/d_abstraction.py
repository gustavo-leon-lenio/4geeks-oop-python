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


#########

import requests


class PokemonAPIClient:
    BASE_URL = "https://pokeapi.co/api/v2"

    def retrieve_pokemon_by_name(self, pokemon_name):
        url = f"{self.BASE_URL}/pokemon/{pokemon_name}"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None

    def list_pokemons(self):
        url = f"{self.BASE_URL}/pokemon/"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None


# Crear una instancia del cliente
pokemon_client = PokemonAPIClient()

# Obtener información de un Pokémon por nombre
pokemon_name = "bulbasaur"
pokemon_data = pokemon_client.retrieve_pokemon_by_name(pokemon_name)
if pokemon_data:
    print(f"Información de {pokemon_name}:")
    print(f"Nombre: {pokemon_data['name']}")
    print(f"Tipo(s): {[t['type']['name'] for t in pokemon_data['types']]}\n")

# Listar Pokémon
pokemons_list = pokemon_client.list_pokemons()
if pokemons_list:
    print("Lista de Pokémon:")
    for pokemon in pokemons_list["results"]:
        print(pokemon["name"])
