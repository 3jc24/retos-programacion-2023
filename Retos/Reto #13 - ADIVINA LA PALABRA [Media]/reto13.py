# Reto #13: Adivina la palabra
#### Dificultad: Media | Publicación: 27/03/23 | Corrección: 03/04/23

## Enunciado

'''
/*
 * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
 * - El juego comienza proponiendo una palabra aleatoria incompleta
 *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
 * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
 *   la palabra a adivinar)
 *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
 *     uno al número de intentos
 *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
 *     al número de intentos
 *   - Si el contador de intentos llega a 0, el jugador pierde
 * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
 * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
 */
'''
import random as r

def palabra_aleatoria() -> str:
    palabras = ("hola", "adios", "gracias","prueba", "juego","avion","ruta","coche")
    numero = r.randint(0,len(palabras)-1)
    print (numero)
    return (palabras[numero])


def slice (palabra:str) -> str:
    final =""
    print (len(palabra))
    for letra in range(0,len(palabra)):
        if letra % 2 != 0:
            final += "_"
        else:
            final += palabra[letra]
    return final
     

def adivina () -> bool:
    aleatoria = palabra_aleatoria()
    print (slice(aleatoria))
    adivina = input ("Introduce palabra a adivinar:")
    return adivina == aleatoria
    

print (adivina())
