class RecetaPebre:
    def __init__(self, tomates, cebollin, cilantro, aji_verde, dientes_de_ajo, limon, sal, aceite):
        self.tomates = tomates
        self.cebollin = cebollin
        self.cilantro = cilantro
        self.aji_verde = aji_verde
        self.dientes_de_ajo = dientes_de_ajo
        self.limon = limon
        self.sal = sal
        self.aceite = aceite

    def preparar(self):
        print("Picando finamente los tomates, la cebollin, el cilantro, el ají verde y el dientes_de_ajo.")
        print("Mezclando todos los ingredientes picados en un tazón.")
        print("Exprimiendo el jugo del limón sobre la mezcla y agregando sal y aceite al gusto.")
        print("Revuelva todo hasta que los ingredientes estén bien mezclados.")
        print("Prueba el Pebre y ajusta el sabor agregando más sal, limón o cilantro si es necesario.")
        print("El Pebre está listo para servir. ¡Disfrútalo con tus platos favoritos!")


# Crear una instancia de la clase RecetaPebre con ingredientes específicos
mi_pebre = RecetaPebre(
    tomates=4,
    cebollin=1,
    cilantro="al gusto",
    aji_verde=1,
    dientes_de_ajo=1,
    limon=1,
    sal="al gusto",
    aceite="al gusto",
)

# Preparar el "Pebre" utilizando la receta específica de la instancia
mi_pebre.preparar()
