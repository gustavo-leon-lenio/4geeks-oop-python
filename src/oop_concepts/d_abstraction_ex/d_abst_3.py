import json
import urllib.request

# Sin abstracción
url = "https://pokeapi.co/api/v2/pokemon/bulbasaur"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
response = urllib.request.urlopen(req)

if response.status == 200:
    data = response.read().decode('utf-8')
    pokemon_data = json.loads(data)
    print(f"Información de {pokemon_data['name']}:")
    print(f"Nombre: {pokemon_data['name']}")
    print(f"Tipo(s): {[t['type']['name'] for t in pokemon_data['types']]}\n")
else:
    print(f"Error: {response.status}")
