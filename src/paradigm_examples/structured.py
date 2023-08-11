# Ilustración de Programacion Estructurada

"""
El paradigma de programación estructurada se enfoca en dividir 
un programa en bloques más pequeños y organizados llamados "procedimientos" o "funciones". 
Estos procedimientos tienen una estructura lineal y se llaman secuencialmente 
para realizar tareas específicas
"""

def reunir_ingredientes():
    tomates = 4
    cebollin = 1
    cilantro = "al gusto"
    aji_verde = 1
    dientes_de_ajo = 2
    limon = 1
    sal = "al gusto"
    aceite = "al gusto"
    comino = "al gusto"
    return tomates, cebollin, cilantro, aji_verde, dientes_de_ajo, limon, sal, aceite, comino

def picar_ingredientes(tomates, cebollin, cilantro, aji_verde, dientes_de_ajo):
    print("Picando finamente los tomates, la cebollin, el cilantro, el aji verde y el dientes_de_ajo.")
    return (tomates, cebollin, cilantro, aji_verde, dientes_de_ajo)

def mezclar_ingredientes(picados, limon, sal, aceite, comino):
    print("Mezclando todos los ingredientes picados en un tazón.")
    tomates, cebollin, cilantro, aji_verde, dientes_de_ajo = picados
    pebre = (tomates, cebollin, cilantro, aji_verde, dientes_de_ajo, limon, sal, aceite, comino)
    return pebre

def ajustar_sabor(pebre):
    print("Prueba el pebre y ajusta el sabor agregando más sal, limón o cilantro si es necesario.")
    return pebre

def preparar_pebre_estructurado():
    tomates, cebollin, cilantro, aji_verde, dientes_de_ajo, limon, sal, aceite = reunir_ingredientes()
    picados = picar_ingredientes(tomates, cebollin, cilantro, aji_verde, dientes_de_ajo)
    pebre = mezclar_ingredientes(picados, limon, sal, aceite)
    pebre_ajustado = ajustar_sabor(pebre)
    return pebre_ajustado

# Llamada a la función para preparar el pebre utilizando programación estructurada
preparar_pebre_estructurado()
