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

## Encapsulación
