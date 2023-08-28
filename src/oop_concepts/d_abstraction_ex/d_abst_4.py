import json
import urllib.request

# Ejemplo super simple de abstracción
# Las bibliotecas y/o librerias
# ya que abstraen la complejidad al proporcionar funciones y clases


class PokemonAPIClient:
    # """Pokemon Api Client"""

    BASE_URL = "https://pokeapi.co/api/v2"
    HEADER = {'User-Agent': 'Mozilla/5.0'}

    def retrieve_pokemon_by_name(self, pokemon_name):
        url = f"{self.BASE_URL}/pokemon/{pokemon_name}"
        req = urllib.request.Request(url, headers=self.HEADER)
        response = urllib.request.urlopen(req)

        if response.status == 200:
            data = response.read().decode('utf-8')
            return json.loads(data)
        else:
            print(f"Error: {response.status}")
            return None

    def list_pokemons(self):
        """THIS Pokemons from URL"""
        url = f"{self.BASE_URL}/pokemon/"
        req = urllib.request.Request(url, headers=self.HEADER)
        response = urllib.request.urlopen(req)

        if response.status == 200:
            data = response.read().decode('utf-8')
            return json.loads(data)
        else:
            print(f"Error: {response.status}")
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
