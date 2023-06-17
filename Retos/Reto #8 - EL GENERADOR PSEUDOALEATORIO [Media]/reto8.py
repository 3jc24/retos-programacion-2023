# Reto #8: El generador pseudoaleatorio
#### Dificultad: Media | Publicación: 20/02/23 | Corrección: 27/02/23

## Enunciado

'''
/*
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
 */
'''
from time import time_ns
from math import sqrt

def aleatorio () -> int:
    return time_ns() % 101


for _ in range(1, 50):
    print (aleatorio())
