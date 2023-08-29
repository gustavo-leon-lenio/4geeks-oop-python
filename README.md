# Charla 4geeks Orientando Objetos en Python y no morir en el intento

## A.K.A Programación Orientada a Objetos con Python 101

¡Bienvenidos a la charla sobre Programación Orientada a Objetos (POO) en Python! En esta charla, exploraremos los conceptos fundamentales de la POO y cómo se aplican en el lenguaje de programación Python.

## Contenido

- [Introducción a la Programación Orientada a Objetos](#introducción-a-la-programación-orientada-a-objetos)
- [Conceptos Básicos](#conceptos-básicos)
- [Clases y Objetos](#clases-y-objetos)
- [Herencia y Polimorfismo](#herencia-y-polimorfismo)
- [Encapsulación](#encapsulación)
- [Ejemplos de Código](#ejemplos-de-código)
- [Recursos Adicionales](#recursos-adicionales)

## Introducción a la Programación Orientada a Objetos

La Programación Orientada a Objetos es un paradigma de programación que se basa en el concepto de "objetos", que son instancias de clases. En esta charla, aprenderemos cómo la POO permite organizar y estructurar nuestro código de manera eficiente y modular.

## Conceptos Básicos

- **Clases**: Las clases son plantillas para crear objetos. Definimos atributos y métodos en una clase para modelar objetos con características y comportamientos específicos.

- **Objetos**: Los objetos son instancias de clases. Representan elementos con propiedades y acciones que podemos realizar sobre ellos.

- **Herencia**:Es una propiedad la cual permite que una clase puede adoptar las características (atributos y métodos) de otra clase.

- **Polimorfismo**:Es La capacidad de diferentes clases (que pueden estar relacionadas a través de la herencia) de responder a una misma llamada de método de manera diferente.

- **Abstracción**:Implica simplificar y representar la complejidad de la realidad de una manera más manejable. En esencia, la abstracción consiste en identificar las características esenciales y relevantes de un objeto o sistema mientras se omiten los detalles menos importantes.

- **Encapsulación**: La encapsulación nos permite ocultar la implementación interna de un objeto y exponer solo una interfaz para interactuar con él.

## Clases y Objetos

En esta sección, exploraremos cómo definir clases y crear objetos en Python:

```python
class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def ladrar(self):
        print(f"{self.nombre} está ladrando.")

mi_perro = Perro("Fido", 3)
mi_perro.ladrar()
```

## Herencia y Polimorfismo

```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def emitir_sonido(self):
        return "Algún sonido genérico"

class Perro(Animal):
    # "Canis familiaris" 🐶
    def emitir_sonido(self):
        return "¡Guau!"

class Gato(Animal):
    # "Felis catus" 🐱
    def emitir_sonido(self):
        return "Miau!"
```

## Abstracción

```python
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

#######
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

# Con abstracción
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
```

## Encapsulación

```python
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

persona = Persona("James", 99)
persona.__nombre ## Attribute Error
```
