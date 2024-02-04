# 1. Importanciones de librerias
import math


# 2. Definimos contantes
PI = 3.14

# 3. Colocar nuestras funciones y/o clases
def area_rectangulo(base:int, altura:int):
    """Calcula el área de un rectangulo según su base y altura"""
    # return -> returno un valor 
    return base * altura


# 4. Nuestro código

# Calcula la area de un rectangulo

base = int(input('Introduce el valor de la base: '))
altura = int(input('Introduce el valor de la altura: '))

# area = base * altura
area = area_rectangulo(base=base, altura=altura)

print(f'El área del rectangulo de base={base} y altura={altura} es {area}')












